from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
#kayıt için register modeli
class Register(models.Model):
    fırst_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254, unique=True)
    password=models.CharField(max_length=128)
    
    def save(self, *args, **kwargs):
        # Şifreyi kaydetmeden önce hashle
        if self.password:
            self.password = make_password(self.password)
        super(Register, self).save(*args, **kwargs)
    def __str__(self):
        return self.first_name
#rezervasyon sistemi modeli 
class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    room_number=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Rezarvasyo{self.user.username} için {self.check_in}-{self.check_out}"

class CreditCard(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    card_number=models.CharField(max_length=16)
    card_name=models.CharField(max_length=100)
    expiry_date=models.CharField(max_length=5)
    cvv=models.CharField(max_length=3)

    def __str__(self):
        return f'{self.card_name}-{self.card_number}'