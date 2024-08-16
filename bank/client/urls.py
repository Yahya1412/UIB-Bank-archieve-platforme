from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
       

urlpatterns = [
    path('',views.index,name="client"), 
    path('ajouter_client',views.ajouter_client,name="ajouter_client"),
    path('modifier_client/<int:id>/', views.client_edit, name='modifier_client'),
    path('client_delete/<int:id>/', views.supprimer_client, name='client_delete'),
    path('export_csv',views.export_csv,name="export_csv"),
    path('home/', views.stats_client, name='home'),

]

