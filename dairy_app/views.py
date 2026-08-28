from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
from django.http import HttpResponse
from django.template.loader import render_to_string

from datetime import date

from xhtml2pdf import pisa

from .models import (
    Cattle,
    MilkProduction,
    Inventory,
    HealthRecord
)

from .forms import (
    CattleForm,
    InventoryForm,
    MilkProductionForm,
    HealthRecordForm
)


# ============================================================
# 1. LOGIN
# ============================================================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:

            auth.login(request, user)

            if user.role == 'Admin':

                return redirect(
                    'admin_dashboard'
                )

            else:

                return redirect(
                    'vet_dashboard'
                )

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid Credentials'
            }
        )

    return render(
        request,
        'login.html'
    )


# ============================================================
# 2. ADMIN DASHBOARD
# ============================================================

@login_required
def admin_dashboard(request):

    if request.user.role != 'Admin':

        return redirect(
            'vet_dashboard'
        )

    today_records = MilkProduction.objects.filter(
        date=date.today()
    )

    milk_sum = sum(
        record.quantity_liters
        for record in today_records
    )

    context = {

        'total_cattle':
            Cattle.objects.count(),

        'inventory_items':
            Inventory.objects.all(),

        'milk_today':
            milk_sum,

        'health_records':
            HealthRecord.objects.count(),
    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )


# ============================================================
# 3. ADD CATTLE
# ============================================================

@login_required
def add_cattle(request):

    if request.user.role != 'Admin':

        return redirect(
            'vet_dashboard'
        )

    form = CattleForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'admin_dashboard'
        )

    return render(
        request,
        'add_cattle.html',
        {
            'form': form
        }
    )


# ============================================================
# 4. ADD INVENTORY
# ============================================================

@login_required
def add_inventory(request):

    if request.user.role != 'Admin':

        return redirect(
            'vet_dashboard'
        )

    form = InventoryForm(
        request.POST or None
    )

    if request.method == 'POST' and form.is_valid():

        form.save()

        return redirect(
            'admin_dashboard'
        )

    return render(
        request,
        'add_inventory.html',
        {
            'form': form
        }
    )


# ============================================================
# 5. LOG MILK
# ============================================================

@login_required
def log_milk(request):

    if request.user.role != 'Admin':

        return redirect(
            'vet_dashboard'
        )

    form = MilkProductionForm(
        request.POST or None
    )

    if request.method == 'POST' and form.is_valid():

        form.save()

        return redirect(
            'admin_dashboard'
        )

    return render(
        request,
        'log_milk.html',
        {
            'form': form
        }
    )


# ============================================================
# 6. VETERINARIAN DASHBOARD
# ============================================================

@login_required
def vet_dashboard(request):

    if request.user.role != 'Vet':

        return redirect(
            'admin_dashboard'
        )

    # --------------------------------------------------------
    # Only records assigned to this veterinarian
    # --------------------------------------------------------

    my_health_records = HealthRecord.objects.filter(
        vet_assigned=request.user
    ).select_related(
        'cattle'
    ).order_by(
        '-checkup_date'
    )

    # --------------------------------------------------------
    # Count records
    # --------------------------------------------------------

    total_records = my_health_records.count()

    # --------------------------------------------------------
    # Today's checkups
    # --------------------------------------------------------

    today_checkups = my_health_records.filter(
        checkup_date=date.today()
    ).count()

    context = {

        'health_records':
            my_health_records,

        'total_records':
            total_records,

        'today_checkups':
            today_checkups,
    }

    return render(
        request,
        'vet_dashboard.html',
        context
    )


# ============================================================
# 7. ADD HEALTH RECORD
# ============================================================

@login_required
def add_health_record(request):

    # Only veterinarian can add health records

    if request.user.role != 'Vet':

        return redirect(
            'admin_dashboard'
        )

    form = HealthRecordForm(
        request.POST or None
    )

    if request.method == 'POST':

        if form.is_valid():

            health_record = form.save(
                commit=False
            )

            # Automatically assign current veterinarian

            health_record.vet_assigned = (
                request.user
            )

            health_record.save()

            # Update cattle health status

            cattle = health_record.cattle

            cattle.health_status = 'Under Treatment'

            cattle.save(
                update_fields=[
                    'health_status'
                ]
            )

            return redirect(
                'vet_dashboard'
            )

    return render(
        request,
        'add_health.html',
        {
            'form': form
        }
    )


# ============================================================
# 8. REPORTS
# ============================================================

@login_required
def reports(request):

    start_date = request.GET.get(
        'start_date'
    )

    end_date = request.GET.get(
        'end_date'
    )

    # --------------------------------------------------------
    # Milk Records
    # --------------------------------------------------------

    milk_records = MilkProduction.objects.select_related(
        'cattle'
    ).order_by(
        '-date'
    )

    if start_date:

        milk_records = milk_records.filter(
            date__gte=start_date
        )

    if end_date:

        milk_records = milk_records.filter(
            date__lte=end_date
        )

    milk_total = milk_records.aggregate(
        total=Sum('quantity_liters')
    )['total'] or 0

    milk_average = milk_records.aggregate(
        average=Avg('quantity_liters')
    )['average'] or 0

    # --------------------------------------------------------
    # Cattle
    # --------------------------------------------------------

    cattle_records = Cattle.objects.all().order_by(
        'tag_id'
    )

    # --------------------------------------------------------
    # Inventory
    # --------------------------------------------------------

    inventory_records = Inventory.objects.all().order_by(
        'item_name'
    )

    # --------------------------------------------------------
    # Health Records
    # --------------------------------------------------------

    health_records = HealthRecord.objects.select_related(
        'cattle',
        'vet_assigned'
    ).order_by(
        '-checkup_date'
    )

    # --------------------------------------------------------
    # If Vet -> only assigned records
    # --------------------------------------------------------

    if request.user.role == 'Vet':

        health_records = health_records.filter(
            vet_assigned=request.user
        )

    context = {

        'milk_records':
            milk_records,

        'milk_total':
            milk_total,

        'milk_average':
            milk_average,

        'cattle_records':
            cattle_records,

        'inventory_records':
            inventory_records,

        'health_records':
            health_records,

        'total_cattle':
            cattle_records.count(),

        'total_inventory':
            inventory_records.count(),

        'total_health_records':
            health_records.count(),

        'start_date':
            start_date or '',

        'end_date':
            end_date or '',

    }

    return render(
        request,
        'reports.html',
        context
    )


# ============================================================
# 9. DOWNLOAD PDF REPORT
# ============================================================

@login_required
def download_report_pdf(request):

    start_date = request.GET.get(
        'start_date'
    )

    end_date = request.GET.get(
        'end_date'
    )

    # --------------------------------------------------------
    # Milk records
    # --------------------------------------------------------

    milk_records = MilkProduction.objects.select_related(
        'cattle'
    ).order_by(
        '-date'
    )

    if start_date:

        milk_records = milk_records.filter(
            date__gte=start_date
        )

    if end_date:

        milk_records = milk_records.filter(
            date__lte=end_date
        )

    milk_total = milk_records.aggregate(
        total=Sum('quantity_liters')
    )['total'] or 0

    milk_average = milk_records.aggregate(
        average=Avg('quantity_liters')
    )['average'] or 0

    # --------------------------------------------------------
    # Other reports
    # --------------------------------------------------------

    cattle_records = Cattle.objects.all().order_by(
        'tag_id'
    )

    inventory_records = Inventory.objects.all().order_by(
        'item_name'
    )

    health_records = HealthRecord.objects.select_related(
        'cattle',
        'vet_assigned'
    ).order_by(
        '-checkup_date'
    )

    # --------------------------------------------------------
    # Vet sees only their records
    # --------------------------------------------------------

    if request.user.role == 'Vet':

        health_records = health_records.filter(
            vet_assigned=request.user
        )

    # --------------------------------------------------------
    # PDF context
    # --------------------------------------------------------

    context = {

        'milk_records':
            milk_records,

        'milk_total':
            milk_total,

        'milk_average':
            milk_average,

        'cattle_records':
            cattle_records,

        'inventory_records':
            inventory_records,

        'health_records':
            health_records,

        'total_cattle':
            cattle_records.count(),

        'total_inventory':
            inventory_records.count(),

        'total_health_records':
            health_records.count(),

        'start_date':
            start_date or '',

        'end_date':
            end_date or '',

    }

    # --------------------------------------------------------
    # Render PDF HTML
    # --------------------------------------------------------

    html_string = render_to_string(
        'report_pdf.html',
        context
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = (
        'attachment; '
        'filename="dairy_farm_report.pdf"'
    )

    pdf_status = pisa.CreatePDF(
        html_string,
        dest=response
    )

    if pdf_status.err:

        return HttpResponse(
            'Error while generating PDF.'
        )

    return response


# ============================================================
# 10. LOGOUT
# ============================================================

def logout_view(request):

    auth.logout(request)

    return redirect(
        'login_view'
    )