from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
       

urlpatterns = [
    path('',views.index,name="user"), 
    path('ajouter_user',views.ajouter_user,name="ajouter_user"),
    path('modifier_user/<int:id>/', views.user_edit, name='modifier_user'),
    path('user_delete/<int:id>/', views.supprimer_user, name='user_delete'),
    path('export_csv',views.export_csv_user,name="export_csv_user"),

]

