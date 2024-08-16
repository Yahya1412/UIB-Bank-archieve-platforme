from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
       

urlpatterns = [
    path('',views.index,name="compte"), 
    path('ajouter_compte',views.ajouter_tache,name="ajouter_compte"),
    path('tachestats',views.stats_compte,name="stats_tache"),
    path('modifier_compte/<int:id>/', views.tache_edit, name='modifier_compte'),
    path('compte_delete/<int:id>/', views.supprimer_tache, name='compte_delete'),
    path('export_csv',views.export_csv_compte,name="export_csv_compte"),
    path('home/', views.stats_compte, name='home'),

]

