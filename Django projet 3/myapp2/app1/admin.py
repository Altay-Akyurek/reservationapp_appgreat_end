from django.contrib import admin
from .models import Register
from .models import Reservation,CreditCard
from .forms import ReservationForm,CreditCardForm

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationForm
    list_display = ('user', 'check_in', 'check_out', 'room_number', 'created_at')  # user alanını ekle
    search_fields = ('user__username', 'room_number')  # Kullanıcı adı üzerinden arama yapabilmek için

admin.site.register(Reservation, ReservationAdmin)

admin.site.register(Register)
class CardAdmin(admin.ModelAdmin):
    form = CreditCardForm
    list_display = ('user', 'card_name', 'card_number', 'expiry_date', 'cvv')
    search_fields = ('user__username', 'card_number')

# Modeli admin paneline kaydetme
admin.site.register(CreditCard, CardAdmin)
