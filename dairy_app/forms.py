from django import forms

from .models import (
    Cattle,
    Inventory,
    MilkProduction,
    HealthRecord
)


# ============================================================
# CATTLE FORM
# ============================================================

class CattleForm(forms.ModelForm):

    class Meta:

        model = Cattle

        fields = [
            'tag_id',
            'breed',
            'birth_date',
            'health_status'
        ]

        widgets = {

            'birth_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'tag_id': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'breed': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'health_status': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


# ============================================================
# INVENTORY FORM
# ============================================================

class InventoryForm(forms.ModelForm):

    class Meta:

        model = Inventory

        fields = [
            'item_name',
            'quantity',
            'unit'
        ]

        widgets = {

            'item_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'unit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. kg, Liters'
                }
            ),
        }


# ============================================================
# MILK PRODUCTION FORM
# ============================================================

class MilkProductionForm(forms.ModelForm):

    class Meta:

        model = MilkProduction

        fields = [
            'cattle',
            'date',
            'quantity_liters'
        ]

        widgets = {

            'cattle': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'quantity_liters': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),
        }


# ============================================================
# HEALTH RECORD FORM
# ============================================================

class HealthRecordForm(forms.ModelForm):

    class Meta:

        model = HealthRecord

        fields = [
            'cattle',
            'checkup_date',
            'diagnosis',
            'treatment'
        ]

        widgets = {

            'cattle': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'checkup_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'diagnosis': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder':
                        'Enter diagnosis'
                }
            ),

            'treatment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder':
                        'Enter treatment details'
                }
            ),
        }