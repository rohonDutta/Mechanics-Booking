from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from . import models

# --- REGEX VALIDATOR ---
# Matches: 2 letters, space, 2 digits, space, 1 letter, space, 4 digits
vehicle_pattern = RegexValidator(
    regex=r'^[A-Za-z]{2}\s\d{2}\s[A-Za-z]{1}\s\d{4}$',
    message='Enter vehicle number in format: "AB 12 C 1234"'
)

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']

class MechanicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class MechanicForm(forms.ModelForm):
    class Meta:
        model = models.Mechanic
        fields = ['address', 'mobile', 'profile_pic', 'skill']

class MechanicSalaryForm(forms.Form):
    salary = forms.IntegerField()

class RequestForm(forms.ModelForm):
    # Overriding vehicle_no to handle alphanumeric input and regex validation
    vehicle_no = forms.CharField(
        validators=[vehicle_pattern],
        widget=forms.TextInput(attrs={'placeholder': 'e.g. WB 12 C 1234', 'class': 'form-control'})
    )

    class Meta:
        model = models.Request
        fields = ['category', 'vehicle_no', 'vehicle_name', 'vehicle_model', 'vehicle_brand', 'problem_description']
        widgets = {
            'problem_description': forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

    # Automatically converts input to uppercase before saving
    def clean_vehicle_no(self):
        return self.cleaned_data['vehicle_no'].upper()

class AdminRequestForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=models.Customer.objects.all(), empty_label="Customer Name", to_field_name='id')
    mechanic = forms.ModelChoiceField(queryset=models.Mechanic.objects.all(), empty_label="Mechanic Name", to_field_name='id')
    cost = forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    mechanic = forms.ModelChoiceField(queryset=models.Mechanic.objects.all(), empty_label="Mechanic Name", to_field_name='id')
    cost = forms.IntegerField()
    stat = (('Pending', 'Pending'), ('Approved', 'Approved'), ('Released', 'Released'))
    status = forms.ChoiceField(choices=stat)

class UpdateCostForm(forms.Form):
    cost = forms.IntegerField()

class MechanicUpdateStatusForm(forms.Form):
    stat = (('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'))
    status = forms.ChoiceField(choices=stat)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['by', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

presence_choices = (('Present', 'Present'), ('Absent', 'Absent'))
class AttendanceForm(forms.Form):
    present_status = forms.ChoiceField(choices=presence_choices)
    date = forms.DateField()

class AskDateForm(forms.Form):
    date = forms.DateField()

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))