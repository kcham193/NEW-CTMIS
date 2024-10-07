from django.contrib import admin
from database.models import Material, MaterialCategory, Course, Member, Module, FeeStructure, FeeSummary

# Register your models here.
admin.site.register (MaterialCategory)
admin.site.register (Material)
admin.site.register (Course)
admin.site.register (Module)
admin.site.register (Member)
admin.site.register(FeeStructure)
admin.site.register(FeeSummary)
