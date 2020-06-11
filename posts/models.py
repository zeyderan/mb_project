from django.db import models

# Create your models here.

# post modeli eklendi 
#veritabanında post isimli bir tablo oluştu
#ve tabloda text isimli bir kolon var

#python manage.py makemigrations posts
#python manage.py migrate
class Post(models.Model):
    text = models.TextField()

    #admin panelinde postlar listesinde görünecek isim 
    # __str__ metodu ile dönndürülür
    def __str__(self):
        #isim olarak text'in ilk 50 karakterini döndür
        return self.text[:50]

