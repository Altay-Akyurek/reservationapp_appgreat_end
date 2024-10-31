from django import forms
from .models import Reservation,CreditCard
from django.contrib.auth.models import User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'room_number']  # uyarı eskiden user adlı bir parematre koydum ama sayfadan alınan bilgilerde isim olmadığından veri tabanına ekleme yapmadı 
class CreditCardForm(forms.ModelForm):
    class Meta:
        model=CreditCard
        fields=['card_number','card_name','expiry_date','cvv']