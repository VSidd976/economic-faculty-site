from django.contrib import admin
from faculty import models

# Register your models here.

admin.site.register(models.Department)
admin.site.register(models.Program)
admin.site.register(models.Lecturer)
admin.site.register(models.MainPageInfo)
