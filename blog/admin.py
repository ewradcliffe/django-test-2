from django.contrib import admin
from .models import Reservation
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('reservation_ref', 'reservation_date', 'reservation_time', 'number_of_guests')
    search_fields = ['reservation_ref']
    list_filter = ('reservation_date',)
 #   prepopulated_fields = {'slug': ('title',)}
  #  summernote_fields = ('content',)

#admin.site.register(Reservation)
