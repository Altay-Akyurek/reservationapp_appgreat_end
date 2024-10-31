
from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('room', views.room, name='room'),
    path('room1', views.room1, name='room1'),
    path('room2', views.room2, name='room2'),
    path('room3', views.room3, name='room3'),
    path('room4', views.room4, name='room4'),
    path('room5', views.room5, name='room5'),
    path('room6', views.room6, name='room6'),
    
    path('loading1', views.loading1, name='loading1'),
    path('loading2', views.loading2, name='loading2'),
    path('loading3', views.loading3, name='loading3'),
    path('loading4', views.loading4, name='loading4'),
    path('loading5', views.loading5, name='loading5'),
    path('loading6', views.loading6, name='loading6'),
    path('sell_loading', views.sell_loading, name='sell_loading'),
    path('loading', views.loading, name='loading'),
    path('yes', views.yes, name='yes'),

    path('sell', views.sell, name='sell'),
    path('', views.user_login, name='user_login'),  # Burada 'name' parametresini ekledim
    path('kayıt', views.user_register,name='user_register'),
    path('rezervasyon_oluştur', views.create_reservation,name='create_reservation'),
    path('liste', views.user_register,name='reservation_list'),
    path('iptal', views.user_register,name='cancel_reservation'),
]