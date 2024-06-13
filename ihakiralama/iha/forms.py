# iha/forms.py
from django import forms
from .models import Iha, Kiralama

class IhaForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = ['marka', 'model', 'agirlik', 'kategori', 'kiralanabilir']

class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = ['iha', 'kiralayan', 'baslangic_tarihi', 'bitis_tarihi']


# iha/forms.py
from django import forms
from .models import Iha, Kiralama

class IhaForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = ['marka', 'model', 'agirlik', 'kategori', 'kiralanabilir']

class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = ['iha', 'baslangic_tarihi', 'bitis_tarihi']


# iha/forms.py
from django import forms
from .models import Iha, Kiralama

class IhaForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = ['marka', 'model', 'agirlik', 'kategori', 'kiralanabilir']

class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = ['iha', 'baslangic_tarihi', 'bitis_tarihi']
        widgets = {
            'baslangic_tarihi': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'bitis_tarihi': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
