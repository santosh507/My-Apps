from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .forms import MyUserCreationForm,MyUserChangeForm
from .models import EmployeeDetails,SkillSet

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeDetailsInline(admin.StackedInline):
    model = EmployeeDetails
    can_delete = False
    verbose_name_plural = 'Details'

# Define a new User admin
class MyUserAdmin(BaseUserAdmin):
    readonly_fields = ('id',)
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    inlines = (EmployeeDetailsInline,)

class EmployeeDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class SkillSetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)
admin.site.register(SkillSet,SkillSetAdmin)