from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SkillSet(models.Model):
    skill_name = models.CharField(max_length=50, null=False, verbose_name='Skills',unique=True)
    skill_version = models.CharField(max_length=10, null=False, verbose_name='Version Used')

    def __str__(self):
        return "{0} Version : {1}".format(self.skill_name,self.skill_version)

class EmployeeDetails(models.Model):
    employee_id = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(SkillSet,verbose_name='Skills')
    phone_no = models.IntegerField(max_length=10, null=False, verbose_name='Phone Number', blank=False)
    pan_no = models.CharField(max_length=10,null=False,verbose_name='PAN No')
    adhaar_no = models.CharField(max_length=10,null=False,verbose_name='Adhaar No')
    dob = models.DateField(verbose_name="Date Of Birth",blank=False)
    skill_proficiency = models.DecimalField(decimal_places=1,max_digits=5, verbose_name='Skill Proficiency (Specify in Years.Months Format)',default=0)
    comment = models.TextField(max_length=50, null=False, verbose_name='Comments', default='', blank=True)

    def __str__(self):
        return "{0}".format(str(self.employee_id))

