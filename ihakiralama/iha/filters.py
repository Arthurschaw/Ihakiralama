# iha/filters.py
import django_filters
from .models import Iha, Kiralama

class IhaFilter(django_filters.FilterSet):
    class Meta:
        model = Iha
        fields = ['marka', 'model', 'agirlik', 'kategori', 'kiralanabilir']

class KiralamaFilter(django_filters.FilterSet):
    class Meta:
        model = Kiralama
        fields = ['iha', 'kiralayan', 'baslangic_tarihi', 'bitis_tarihi']
