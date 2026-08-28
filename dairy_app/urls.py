from django.urls import path
from . import views


urlpatterns = [

    # Login
    path(
        '',
        views.login_view,
        name='login_view'
    ),

    # Admin
    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    # Veterinarian
    path(
        'vet-dashboard/',
        views.vet_dashboard,
        name='vet_dashboard'
    ),

    # Cattle
    path(
        'add-cattle/',
        views.add_cattle,
        name='add_cattle'
    ),

    # Inventory
    path(
        'add-inventory/',
        views.add_inventory,
        name='add_inventory'
    ),

    # Milk
    path(
        'log-milk/',
        views.log_milk,
        name='log_milk'
    ),

    # Health Records
    path(
        'add-health/',
        views.add_health_record,
        name='add_health_record'
    ),

    # Reports
    path(
        'reports/',
        views.reports,
        name='reports'
    ),

    # PDF
    path(
        'reports/download-pdf/',
        views.download_report_pdf,
        name='download_report_pdf'
    ),

    # Logout
    path(
        'logout/',
        views.logout_view,
        name='logout_view'
    ),
]