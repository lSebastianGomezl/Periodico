from click import edit
from django.contrib import admin
from .models import Notice
# Register your models here.

class NoiticeAdmin(admin.ModelAdmin):
    list_display= ["id_notice","first_name","type_notice"]
    list_editable = ["first_name"]
    search_fields = ["type_notice"]

admin.site.register(Notice, NoiticeAdmin)