from django.urls import path
from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/name/', views.NameView.as_view(), name = 'name'),
    path('<int:donor_id>/points/', views.points, name = 'points'),
    path('search/', views.SearchResultView.as_view(), name='searchresult')
]