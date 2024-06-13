# iha/tables.py
import django_tables2 as tables
from .models import Iha, Kiralama

class IhaTable(tables.Table):
    class Meta:
        model = Iha
        template_name = "django_tables2/bootstrap.html"
        fields = ("marka", "model", "agirlik", "kategori", "kiralanabilir")

class KiralamaTable(tables.Table):
    class Meta:
        model = Kiralama
        template_name = "django_tables2/bootstrap.html"
        fields = ("iha", "kiralayan", "baslangic_tarihi", "bitis_tarihi")
