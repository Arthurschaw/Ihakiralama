# iha/models.py
from django.db import models
class Iha(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.DecimalField(max_digits=5, decimal_places=2)
    kategori = models.CharField(max_length=100)
    kiralanabilir = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marka} {self.model}"

class Kiralama(models.Model):
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    kiralayan = models.CharField(max_length=100)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()

    def __str__(self):
        return f"{self.kiralayan} - {self.iha.marka} {self.iha.model}"
from django.db import models

# Create your models here.

# iha/models.py
from django.contrib.auth.models import User
from django.db import models

class Iha(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.DecimalField(max_digits=5, decimal_places=2)
    kategori = models.CharField(max_length=100)
    kiralanabilir = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marka} {self.model}"

class Kiralama(models.Model):
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    kiralayan = models.ForeignKey(User, on_delete=models.CASCADE)
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()

    def __str__(self):
        return f"{self.kiralayan.username} - {self.iha.marka} {self.iha.model}"


# iha/models.py
from django.contrib.auth.models import User
from django.db import models

class Iha(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.DecimalField(max_digits=5, decimal_places=2)
    kategori = models.CharField(max_length=100)
    kiralanabilir = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marka} {self.model}"

class Kiralama(models.Model):
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE)
    kiralayan = models.ForeignKey(User, on_delete=models.CASCADE)
    baslangic_tarihi = models.DateTimeField()
    bitis_tarihi = models.DateTimeField()

    def __str__(self):
        return f"{self.kiralayan.username} - {self.iha.marka} {self.iha.model}"
