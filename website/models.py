from django.db import models

# Create your models here.
# Dont worry about the conversion python will automatically convert to DB language

class Record(models.Model):
    # Keeps track of when a 'Record' was created
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
    # ! After creating, run 
    # todo - `python manage.py makemigrations`
    # then to send to the DB
    # todo - `python manage.py migrate`

    # ! Implement users to admin page by going to admin.py & put
    # todo - `from .models import Record`