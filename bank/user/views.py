from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.shortcuts import redirect
from .models import  Utilisateur, Genre, Depart
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import csv
from datetime import datetime

@login_required(login_url='/authent/login/')
def index(request):
    depart = Depart.objects.all()
    genre = Genre.objects.all()
    user = Utilisateur.objects.order_by('nom')
    paginator = Paginator(user,7)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    context={
        'user': user,
        'genre': genre,
        'depart': depart,
        'page_obj': page_obj,
    }
    return render(request, 'user/index.html', context)
@login_required(login_url='/authent/login/')

def ajouter_user(request):
    depart = Depart.objects.all()
    genre = Genre.objects.all()
    user = Utilisateur.objects.all()

    context = {
        'user': user,
        'genre': genre,
        'depart': depart,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'user/ajouter_user.html', context)

    if request.method == 'POST':
        ident = request.POST['ident']
        if not ident:
            messages.warning(request, 'Le champ Identifiant utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)

        nom = request.POST['nom']
        if not nom:
            messages.warning(request, 'Le champ Nom Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)

        prenom = request.POST['prenom']
        if not prenom:
            messages.warning(request, 'Le champ Prénom Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)
        email = request.POST['email']
        if not email:
            messages.warning(request, 'Le champ Adresse mail Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)

        num_tel = request.POST['num_tel']
        if not num_tel:
            messages.warning(request, 'Le champ Numéro du téléphone Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)

        genre = request.POST['genre']
        if not genre:
            messages.warning(request, 'Le champ Genre Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)
        depart = request.POST['depart']
        if not depart:
            messages.warning(request, 'Le champ Département Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)
        salaire = request.POST['salaire']
        if not salaire:
            messages.warning(request, 'Le champ Salaire Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)
        date_naissance = request.POST['date_naissance']
        if not date_naissance:
            messages.warning(request, 'Le champ Date Naissance Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)
        date_recrut = request.POST['date_recrut']
        if not date_recrut:
            messages.warning(request, 'Le champ Date récrutement Utilisateur est nécessaire')
            return render(request, 'user/ajouter_user.html', context)

        

        Utilisateur.objects.create(
            ident=ident,
            nom=nom,
            prenom=prenom,
            email=email,
            num_tel=num_tel,
            genre=genre,
            depart=depart,
            salaire=salaire,
            date_naissance=date_naissance,
            date_recrut=date_recrut,
        )

        messages.success(request, 'Utilisateur enregistrée avec succès')
        return redirect('user')


@login_required(login_url='/authent/login/')


def user_edit(request, id):
    user = Utilisateur.objects.get(pk=id)
    depart = Depart.objects.all()
    genre = Genre.objects.all()
    context ={
        'user': user,
        'values' : user,
        'genre': genre,
        'depart': depart,
    }

    if request.method == 'GET':
        return render(request, 'user/modifier_user.html', context)

    if request.method == 'POST':
        ident = request.POST['ident']
        if not ident:
            messages.warning(request, 'Le champ Identifiant utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)

        nom = request.POST['nom']
        if not nom:
            messages.warning(request, 'Le champ Nom Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)

        prenom = request.POST['prenom']
        if not prenom:
            messages.warning(request, 'Le champ Prénom Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)
        email = request.POST['email']
        if not email:
            messages.warning(request, 'Le champ Adresse mail Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)

        num_tel = request.POST['num_tel']
        if not num_tel:
            messages.warning(request, 'Le champ Numéro du téléphone Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)

        genre = request.POST['genre']
        if not genre:
            messages.warning(request, 'Le champ Genre Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)
        depart = request.POST['depart']
        if not depart:
            messages.warning(request, 'Le champ Département Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)
        salaire = request.POST['salaire']
        if not salaire:
            messages.warning(request, 'Le champ Salaire Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)
        date_naissance = request.POST['date_naissance']
        if not date_naissance:
            messages.warning(request, 'Le champ Date Naissance Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)
        date_recrut = request.POST['date_recrut']
        if not date_recrut:
            messages.warning(request, 'Le champ Date récrutement Utilisateur est nécessaire')
            return render(request, 'user/modifier_user.html', context)

        user.ident = ident
        user.nom = nom
        user.prenom = prenom                     
        user.email = email
        user.num_tel = num_tel
        user.genre = genre
        user.depart = depart
        user.salaire = salaire
        user.date_naissance = date_naissance
        user.date_recrut = date_recrut
        user.save()

        messages.success(request, 'Modification enregistrée avec succès')
        return redirect('user')

@login_required(login_url='/authent/login/')
def supprimer_user(request, id):
    user = Utilisateur.objects.get(pk=id)
    user.delete()
    messages.success(request,'Utilisateur supprimer avec succés')
    return redirect('user')
def export_csv_user(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Utilisateur.csv'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Prénom', 'Adresse Mail', 'Numéro de téléphone', 'Genre', 'Departement', 'Salaire', 'Date Naissance', 'Date de récrutement'])
    user = Utilisateur.objects.all()
    for user in user:
        writer.writerow([user.nom, user.prenom, user.email, user.num_tel, user.genre, user.depart, user.salaire, user.date_naissance, user.date_recrut])
    return response