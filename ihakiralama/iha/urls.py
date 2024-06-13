# iha/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.iha_list, name='iha_list'),
    path('iha/<int:pk>/', views.iha_detail, name='iha_detail'),
    path('iha/new/', views.iha_create, name='iha_create'),
    path('iha/<int:pk>/edit/', views.iha_update, name='iha_update'),
    path('iha/<int:pk>/delete/', views.iha_delete, name='iha_delete'),
    path('kiralama/new/', views.kiralama_create, name='kiralama_create'),
]

# iha/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.iha_list, name='iha_list'),
    path('iha/<int:pk>/', views.iha_detail, name='iha_detail'),
    path('iha/new/', views.iha_create, name='iha_create'),
    path('iha/<int:pk>/edit/', views.iha_update, name='iha_update'),
    path('iha/<int:pk>/delete/', views.iha_delete, name='iha_delete'),
    path('kiralama/new/', views.kiralama_create, name='kiralama_create'),
    path('kiralamalar/', views.kiralama_list, name='kiralama_list'),
]

# iha/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.iha_list, name='iha_list'),
    path('iha/<int:pk>/', views.iha_detail, name='iha_detail'),
    path('iha/new/', views.iha_create, name='iha_create'),
    path('iha/<int:pk>/edit/', views.iha_update, name='iha_update'),
    path('iha/<int:pk>/delete/', views.iha_delete, name='iha_delete'),
    path('kiralama/new/', views.kiralama_create, name='kiralama_create'),
    path('kiralamalar/', views.kiralama_list, name='kiralama_list'),
    path('kiralama/<int:pk>/edit/', views.kiralama_update, name='kiralama_update'),
    path('kiralama/<int:pk>/delete/', views.kiralama_delete, name='kiralama_delete'),
]

# iha/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.iha_list, name='iha_list'),
    path('iha/<int:pk>/', views.iha_detail, name='iha_detail'),
    path('iha/new/', views.iha_create, name='iha_create'),
    path('iha/<int:pk>/edit/', views.iha_update, name='iha_update'),
    path('iha/<int:pk>/delete/', views.iha_delete, name='iha_delete'),
    path('kiralama/new/', views.kiralama_create, name='kiralama_create'),
    path('kiralamalar/', views.kiralama_list, name='kiralama_list'),
    path('kiralama/<int:pk>/edit/', views.kiralama_update, name='kiralama_update'),
    path('kiralama/<int:pk>/delete/', views.kiralama_delete, name='kiralama_delete'),
]


# iha/urls.py
from django.urls import path
from .views import IhaListView, KiralamaListView, kiralama_create, kiralama_update, kiralama_delete

urlpatterns = [
    path('', IhaListView.as_view(), name='iha_list'),
    path('kiralamalar/', KiralamaListView.as_view(), name='kiralama_list'),
    path('kiralama/new/', kiralama_create, name='kiralama_create'),
    path('kiralama/<int:pk>/edit/', kiralama_update, name='kiralama_update'),
    path('kiralama/<int:pk>/delete/', kiralama_delete, name='kiralama_delete'),
]
