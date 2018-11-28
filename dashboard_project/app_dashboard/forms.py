from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class MyUserCreationForm(UserCreationForm):
    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            raise ValidationError("First name is required.")
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]

    def clean_email(self):
        if self.cleaned_data["email"].strip() == '':
            raise ValidationError("Email address is required.")
        return self.cleaned_data["email"]

    def clean_dob(self):
        if self.cleaned_data["dob"].strip() == '':
            raise ValidationError("Date of birth is required.")
        return self.cleaned_data["dob"]

    def clean_phone_no(self):
        if self.cleaned_data["phone_no"].strip() == '':
            raise ValidationError("Phone number is required.")
        return self.cleaned_data["phone_no"]

class MyUserChangeForm(UserChangeForm):
    def clean_first_name(self):
        if self.cleaned_data["first_name"].strip() == '':
            raise ValidationError("First name is required.")
        return self.cleaned_data["first_name"]

    def clean_last_name(self):
        if self.cleaned_data["last_name"].strip() == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]

    def clean_email(self):
        if self.cleaned_data["email"].strip() == '':
            raise ValidationError("Email address is required.")
        return self.cleaned_data["email"]

    def clean_dob(self):
        if self.cleaned_data["dob"].strip() == '':
            raise ValidationError("Date of birth is required.")
        return self.cleaned_data["dob"]

    def clean_phone_no(self):
        if self.cleaned_data["phone_no"].strip() == '':
            raise ValidationError("Phone number is required.")
        return self.cleaned_data["phone_no"]