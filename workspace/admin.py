from django.contrib import admin

from workspace.models import Query
# Register your models here.

# Декоратор с помощью которого в админке отображаются указанные поля
@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
