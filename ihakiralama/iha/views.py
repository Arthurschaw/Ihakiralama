# iha/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Iha, Kiralama
from .forms import IhaForm, KiralamaForm
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import Iha, Kiralama
from .tables import IhaTable, KiralamaTable
from .filters import IhaFilter, KiralamaFilter

class IhaListView(SingleTableMixin, FilterView):
    table_class = IhaTable
    model = Iha
    template_name = "iha/iha_list.html"
    filterset_class = IhaFilter

class KiralamaListView(SingleTableMixin, FilterView):
    table_class = KiralamaTable
    model = Kiralama
    template_name = "iha/kiralama_list.html"
    filterset_class = KiralamaFilter
def iha_list(request):
    ihalar = Iha.objects.all()
    return render(request, 'iha/iha_list.html', {'ihalar': ihalar})

def iha_detail(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    return render(request, 'iha/iha_detail.html', {'iha': iha})

def iha_create(request):
    if request.method == "POST":
        form = IhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IhaForm()
    return render(request, 'iha/iha_form.html', {'form': form})

def iha_update(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    if request.method == "POST":
        form = IhaForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IhaForm(instance=iha)
    return render(request, 'iha/iha_form.html', {'form': form})

def iha_delete(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    if request.method == "POST":
        iha.delete()
        return redirect('iha_list')
    return render(request, 'iha/iha_confirm_delete.html', {'iha': iha})

def kiralama_create(request):
    if request.method == "POST":
        form = KiralamaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = KiralamaForm()
    return render(request, 'iha/kiralama_form.html', {'form': form})
from django.shortcuts import render

# Create your views here.


# iha/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Iha, Kiralama
from .forms import IhaForm, KiralamaForm

def iha_list(request):
    ihalar = Iha.objects.all()
    return render(request, 'iha/iha_list.html', {'ihalar': ihalar})

def iha_detail(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    return render(request, 'iha/iha_detail.html', {'iha': iha})

@login_required
def iha_create(request):
    if request.method == "POST":
        form = IhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IhaForm()
    return render(request, 'iha/iha_form.html', {'form': form})

@login_required
def iha_update(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    if request.method == "POST":
        form = IhaForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IhaForm(instance=iha)
    return render(request, 'iha/iha_form.html', {'form': form})

@login_required
def iha_delete(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    if request.method == "POST":
        iha.delete()
        return redirect('iha_list')
    return render(request, 'iha/iha_confirm_delete.html', {'iha': iha})

@login_required
def kiralama_create(request):
    if request.method == "POST":
        form = KiralamaForm(request.POST)
        if form.is_valid():
            kiralama = form.save(commit=False)
            kiralama.kiralayan = request.user
            kiralama.save()
            return redirect('iha_list')
    else:
        form = KiralamaForm()
    return render(request, 'iha/kiralama_form.html', {'form': form})

@login_required
def kiralama_list(request):
    kiralamalar = Kiralama.objects.filter(kiralayan=request.user)
    return render(request, 'iha/kiralama_list.html', {'kiralamalar': kiralamalar})


# iha/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Iha, Kiralama
from .forms import IhaForm, KiralamaForm

def iha_list(request):
    ihalar = Iha.objects.all()
    return render(request, 'iha/iha_list.html', {'ihalar': ihalar})

def iha_detail(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    return render(request, 'iha/iha_detail.html', {'iha': iha})

@login_required
def iha_create(request):
    if request.method == "POST":
        form = IhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IhaForm()
    return render(request, 'iha/iha_form.html', {'form': form})

@login_required
def iha_update(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    if request.method == "POST":
        form = IhaForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IhaForm(instance=iha)
    return render(request, 'iha/iha_form.html', {'form': form})

@login_required
def iha_delete(request, pk):
    iha = get_object_or_404(Iha, pk=pk)
    if request.method == "POST":
        iha.delete()
        return redirect('iha_list')
    return render(request, 'iha/iha_confirm_delete.html', {'iha': iha})

@login_required
def kiralama_create(request):
    if request.method == "POST":
        form = KiralamaForm(request.POST)
        if form.is_valid():
            kiralama = form.save(commit=False)
            kiralama.kiralayan = request.user
            kiralama.save()
            return redirect('kiralama_list')
    else:
        form = KiralamaForm()
    return render(request, 'iha/kiralama_form.html', {'form': form})

@login_required
def kiralama_list(request):
    kiralamalar = Kiralama.objects.filter(kiralayan=request.user)
    return render(request, 'iha/kiralama_list.html', {'kiralamalar': kiralamalar})

@login_required
def kiralama_update(request, pk):
    kiralama = get_object_or_404(Kiralama, pk=pk)
    if request.method == "POST":
        form = KiralamaForm(request.POST, instance=kiralama)
        if form.is_valid():
            form.save()
            return redirect('kiralama_list')
    else:
        form = KiralamaForm(instance=kiralama)
    return render(request, 'iha/kiralama_form.html', {'form': form})

@login_required
def kiralama_delete(request, pk):
    kiralama = get_object_or_404(Kiralama, pk=pk)
    if request.method == "POST":
        kiralama.delete()
        return redirect('kiralama_list')
    return render(request, 'iha/kiralama_confirm_delete.html', {'kiralama': kiralama})


# iha/views.py
from django.contrib import messages

@login_required
def kiralama_create(request):
    if request.method == "POST":
        form = KiralamaForm(request.POST)
        if form.is_valid():
            kiralama = form.save(commit=False)
            kiralama.kiralayan = request.user
            # İHA'nın belirtilen tarihlerde zaten kiralanıp kiralanmadığını kontrol et
            overlap_exists = Kiralama.objects.filter(
                iha=kiralama.iha,
                baslangic_tarihi__lt=kiralama.bitis_tarihi,
                bitis_tarihi__gt=kiralama.baslangic_tarihi
            ).exists()
            if overlap_exists:
                messages.error(request, "Seçilen tarihlerde bu İHA zaten kiralanmış.")
            else:
                kiralama.save()
                messages.success(request, "Kiralama işlemi başarıyla tamamlandı.")
                return redirect('kiralama_list')
    else:
        form = KiralamaForm()
    return render(request, 'iha/kiralama_form.html', {'form': form})

@login_required
def kiralama_update(request, pk):
    kiralama = get_object_or_404(Kiralama, pk=pk)
    if request.method == "POST":
        form = KiralamaForm(request.POST, instance=kiralama)
        if form.is_valid():
            # İHA'nın belirtilen tarihlerde zaten kiralanıp kiralanmadığını kontrol et
            overlap_exists = Kiralama.objects.filter(
                iha=form.cleaned_data['iha'],
                baslangic_tarihi__lt=form.cleaned_data['bitis_tarihi'],
                bitis_tarihi__gt=form.cleaned_data['baslangic_tarihi']
            ).exclude(pk=pk).exists()
            if overlap_exists:
                messages.error(request, "Seçilen tarihlerde bu İHA zaten kiralanmış.")
            else:
                form.save()
                messages.success(request, "Kiralama işlemi başarıyla güncellendi.")
                return redirect('kiralama_list')
    else:
        form = KiralamaForm(instance=kiralama)
    return render(request, 'iha/kiralama_form.html', {'form': form})


# iha/views.py
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import Iha, Kiralama
from .tables import IhaTable, KiralamaTable
from .filters import IhaFilter, KiralamaFilter

class IhaListView(SingleTableMixin, FilterView):
    table_class = IhaTable
    model = Iha
    template_name = "iha/iha_list.html"
    filterset_class = IhaFilter

class KiralamaListView(SingleTableMixin, FilterView):
    table_class = KiralamaTable
    model = Kiralama
    template_name = "iha/kiralama_list.html"
    filterset_class = KiralamaFilter
