from django.contrib import admin
from .models import Client, Genre, Nationalité, Statut_mat, Nbr_per
admin.site.register(Client)
admin.site.register(Genre)
admin.site.register(Nationalité)
admin.site.register(Statut_mat)
admin.site.register(Nbr_per)


