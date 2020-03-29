from django.urls import path
from . import views

app_name = 'notp'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('search/', views.SearchResultView.as_view(), name='searchresult'),
    path('form/', views.form, name='form'),
]