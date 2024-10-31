from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ReservationForm,CreditCardForm
from .models import Reservation
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")
def user_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login (request,user)
            return render(request,"loading/open_loading.html")
        else:
            return render(request,"login.html",{"error":"username ya da parola yanlış girilmiştir"})
    else:
        return render(request,"login.html")
    
def room(request):
    return render(request,"reservation_list.html")
       

def room1(request):
    return render(request,"Luxury_Suite.html")
def room2(request):
    return render(request,"Delux_Suite.html")
def room3(request):
    return render(request,"Premier_Suite.html")
def room4(request):
    return render(request,"Luxury_Room.html")
def room5(request):
    return render(request,"Delux_Room.html")
def room6(request):
    return render(request,"Premier_Room.html")

def loading(request):
    return render(request,"loading/open_loading.html")

def loading1(request):
    return render(request,"loading/room_loading.html")

def loading2(request):
    return render(request,"loading/room1_loading.html")
def loading3(request):
    return render(request,"loading/room3_loading.html")
def loading4(request):
    return render(request,"loading/room4_loading.html")
def loading5(request):
    return render(request,"loading/room5_loading.html")
def loading6(request):
    return render(request,"loading/room6_loading.html")

def sell_loading(request):
    return render(request,"loading/sell_loading.html")
def yes(request):
    return render(request,"loading/yes_loading.html")

def sell(request):
    if request.method== 'POST':
        form=CreditCardForm(request.POST)
        if form.is_valid():
            credit_card=form.save(commit=False)
            credit_card.user=request.user
            credit_card.save()
            return redirect('yes')
    else:
        form=CreditCardForm()
    return render(request,'sell.html',{'form':form})

def user_register(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"login.html",{"error":"username kullanılıyor.."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"login.html",{"error":"bu email adresinden önceden kayıt yapılmıştır.."})
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    return render(request,"login.html") #bu yönlendirme değiştirilmiştir
        else:
            return render(request,"login.html",{"error":"parolayı yanlış ya da eksik tuşladınız"})
    else:
        return render(request,"login.html")
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user  # Kullanıcıyı ilişkilendir
            reservation.save()  # Veritabanına kaydet
            messages.success(request, 'Rezervasyon başarıyla oluşturuldu.')
            return redirect('sell_loading')  # Başka bir sayfaya yönlendirme
        else:
            messages.error(request, 'Formda hata var, lütfen kontrol edin.')
    else:
        form = ReservationForm()

    return render(request, 'index.html', {'form': form})  # Formu render et
            
def reservation_list(request):
    reservations=Reservation.objects.filter(user=request.user)
    return render(request,'reservation_list.html',{'reservations':reservations})

def cancel_reservation(request, reservation_id):
    reservation=Reservation.objects.get(id=reservation_id,user=request.user)
    if reservation:
        reservation.delete()
        messages.success(request,'Rezarvosyonunuz Başarılı Bir Şekilde İptal Edildi..')

    else:
        messages.error(request,'Rezervasyonununuz Bulunmadı..')
    return redirect('reservation_list')
    