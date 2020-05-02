from django.contrib import admin

from .models import Flat, Report, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ['created_at']
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_phone_pure')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ('report_flat', 'report_owner')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owners_flats',)
    list_display = ('name', 'pure_phone_number')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Owner, OwnerAdmin)
