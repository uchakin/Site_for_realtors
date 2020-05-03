from django.contrib import admin

from .models import Flat, Report, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ['created_at']
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', 'owners')


class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ('report_flat', 'report_owner')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owners_flats',)
    list_display = ('name', 'pure_phone_number')
    search_fields = ('name',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Owner, OwnerAdmin)
