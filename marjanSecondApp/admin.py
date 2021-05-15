from django.contrib import admin
from .models import School, Faculty, CertificateType, Department, Grade, Student


# Register your models here.
admin.site.register (School)
admin.site.register(Faculty)
admin.site.register(CertificateType)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Student)