from django.contrib import admin

from .models import mentors, employee, technical_board
# Register your models here.

admin.site.register(mentors)
admin.site.register(employee)
admin.site.register(technical_board)