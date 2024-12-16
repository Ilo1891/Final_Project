from django.contrib import admin

from reservation.models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class TableAdmin(admin.ModelAdmin):
    pass