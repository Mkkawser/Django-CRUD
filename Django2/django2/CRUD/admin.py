from django.contrib import admin

from CRUD.models import crudDB


class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'namedb', 'emaildb', 'phonedb')


admin.site.register(crudDB, NameAdmin)
