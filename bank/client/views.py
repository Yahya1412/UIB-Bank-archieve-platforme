from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.shortcuts import redirect
from .models import  Client, Genre, Nationalité, Statut_mat, Nbr_per
from compte.models import  Compte
from user.models import  Utilisateur
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import csv
from datetime import datetime


@login_required(login_url='/authent/login/')
def index(request):
    nbr_per = Nbr_per.objects.all()
    statut_mat = Statut_mat.objects.all()
    nationalité = Nationalité.objects.all()
    genre = Genre.objects.all()
    client = Client.objects.order_by('nom')
    paginator = Paginator(client,7)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    context={
        'client': client,
        'genre': genre,
        'nationalité': nationalité,
        'statut_mat': statut_mat,
        'nbr_per': nbr_per,
        'page_obj': page_obj,
    }
    return render(request, 'client/index.html', context)
@login_required(login_url='/authent/login/')

def ajouter_client(request):
    nbr_per = Nbr_per.objects.all()
    statut_mat = Statut_mat.objects.all()
    nationalité = Nationalité.objects.all()
    genre = Genre.objects.all()
    client = Client.objects.all()

    context = {
        'client': client,
        'genre': genre,
        'nationalité': nationalité,
        'statut_mat': statut_mat,
        'nbr_per': nbr_per,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'client/ajouter_client.html', context)

    if request.method == 'POST':
        first = request.POST['ident']
        if not first:
            messages.warning(request, 'Le champ Identifiant du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)

        nom = request.POST['nom']
        if not nom:
            messages.warning(request, 'Le champ Nom du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)

        prenom = request.POST['prenom']
        if not prenom:
            messages.warning(request, 'Le champ Prénom du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        adresse = request.POST['adresse']
        if not adresse:
            messages.warning(request, 'Le champ Adresse du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        email = request.POST['email']
        if not email:
            messages.warning(request, 'Le champ Adresse mail du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)

        num_tel = request.POST['num_tel']
        if not num_tel:
            messages.warning(request, 'Le champ Numéro du téléphone du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)

        genre = request.POST['genre']
        if not genre:
            messages.warning(request, 'Le champ Genre du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        nationalité = request.POST['nationalité']
        if not nationalité:
            messages.warning(request, 'Le champ Nationalité du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        profession = request.POST['profession']
        if not profession:
            messages.warning(request, 'Le champ Profession du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        statut_mat = request.POST['statut_mat']
        if not statut_mat:
            messages.warning(request, 'Le champ Statut matrimonial du client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        nbr_per = request.POST['nbr_per']
        if not nbr_per:
            messages.warning(request, 'Le champ Nombre de personne en charge est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        revenue_annuel = request.POST['revenue_annuel']
        if not revenue_annuel:
            messages.warning(request, 'Le champ Revenue annuel du Client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)
        date_naissance = request.POST['date_naissance']
        if not date_naissance:
            messages.warning(request, 'Le champ Date de naissance du Client est nécessaire')
            return render(request, 'client/ajouter_client.html', context)

        

        Client.objects.create(
            first=first,
            nom=nom,
            prenom=prenom,
            adresse=adresse,
            email=email,
            num_tel=num_tel,
            genre=genre,
            nationalité=nationalité,
            profession=profession,
            statut_mat=statut_mat,
            nbr_per=nbr_per,
            revenue_annuel=revenue_annuel,
            date_naissance=date_naissance,
        )

        messages.success(request, 'Client enregistrée avec succès')
        return redirect('client')


@login_required(login_url='/authent/login/')


def client_edit(request, id):
    client = Client.objects.get(pk=id)
    nbr_per = Nbr_per.objects.all()
    statut_mat = Statut_mat.objects.all()
    nationalité = Nationalité.objects.all()
    genre = Genre.objects.all()
    context ={
        'client' : client,
        'values' : client,
        'genre': genre,
        'nationalité': nationalité,
        'statut_mat': statut_mat,
        'nbr_per': nbr_per,
    }

    if request.method == 'GET':
        return render(request, 'client/modifier_client.html', context)

    if request.method == 'POST':
        first = request.POST['ident']
        if not first:
            messages.warning(request, 'Le champ Identifiant du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)

        nom = request.POST['nom']
        if not nom:
            messages.warning(request, 'Le champ Nom du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)

        prenom = request.POST['prenom']
        if not prenom:
            messages.warning(request, 'Le champ Prénom du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        adresse = request.POST['adresse']
        if not adresse:
            messages.warning(request, 'Le champ Adresse du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        email = request.POST['email']
        if not email:
            messages.warning(request, 'Le champ Adresse mail du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)

        num_tel = request.POST['num_tel']
        if not num_tel:
            messages.warning(request, 'Le champ Numéro du téléphone du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)

        genre = request.POST['genre']
        if not genre:
            messages.warning(request, 'Le champ Genre du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        nationalité = request.POST['nationalité']
        if not nationalité:
            messages.warning(request, 'Le champ Nationalité du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        profession = request.POST['profession']
        if not profession:
            messages.warning(request, 'Le champ Profession du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        statut_mat = request.POST['statut_mat']
        if not statut_mat:
            messages.warning(request, 'Le champ Statut matrimonial du client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        nbr_per = request.POST['nbr_per']
        if not nbr_per:
            messages.warning(request, 'Le champ Nombre de personne en charge est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        revenue_annuel = request.POST['revenue_annuel']
        if not revenue_annuel:
            messages.warning(request, 'Le champ Revenue annuel du Client est nécessaire')
            return render(request, 'client/modifier_client.html', context)
        date_naissance = request.POST['date_naissance']
        if not date_naissance:
            messages.warning(request, 'Le champ Date de naissance du Client est nécessaire')
            return render(request, 'client/modifier_client.html', context)

        client.first = first
        client.nom = nom
        client.prenom = prenom                     
        client.adresse = adresse
        client.email = email
        client.num_tel = num_tel
        client.genre = genre
        client.nationalité = nationalité
        client.profession = profession
        client.statut_mat = statut_mat
        client.nbr_per = nbr_per
        client.revenue_annuel = revenue_annuel
        client.date_naissance = date_naissance
        client.save()

        messages.success(request, 'Modification enregistrée avec succès')
        return redirect('client')

@login_required(login_url='/authent/login/')
def supprimer_client(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    messages.success(request,'Client supprimer avec succés')
    return redirect('client')
@login_required(login_url='/authent/login/')
def stats_client(request):
    client = Client.objects.all()
    trm = Client.objects.filter(genre = 'Masculin').count()
    trm =int(trm)
    rep = Client.objects.filter(genre = 'Féminin').count()
    rep =int(rep)
    ann = Client.objects.filter(nationalité = 'Tunisie').count()
    ann =int(ann)
    enc = Client.objects.filter(nationalité = 'Algérie').count()
    enc =int(enc)
    att = Client.objects.filter(nationalité = 'Libye').count()
    att =int(att)
    eur = Client.objects.filter(nationalité = 'Européen').count()
    eur =int(eur)
    afr = Client.objects.filter(nationalité = 'Afrique subsaharienne').count()
    afr =int(afr)
    gol = Client.objects.filter(nationalité = 'Pays du golf et Moyen orient').count()
    gol =int(gol)
    atr = Client.objects.filter(nationalité = 'Autre').count()
    atr =int(atr)
    compte = Compte.objects.all()
    trn = Compte.objects.filter(type = 'Compte jeune').count()
    trn =int(trn)
    req = Compte.objects.filter(type = 'Compte chèque').count()
    req =int(req)
    an = Compte.objects.filter(type = 'Compte épargne').count()
    an =int(an)
    en = Compte.objects.filter(type = 'Compte courant').count()
    en =int(en)
    at = Compte.objects.filter(etat = 'Compte Fermé').count()
    at =int(at)
    eu = Compte.objects.filter(etat = 'Compte Bloqué').count()
    eu =int(eu)
    af = Compte.objects.filter(etat = 'Compte Actif').count()
    af =int(af)

    uset = Utilisateur.objects.all()
    tr = Utilisateur.objects.filter(depart = 'Département des opérations bancaires').count()
    tr =int(tr)
    re = Utilisateur.objects.filter(depart = 'Département des prêts').count()
    re =int(re)
    any = Utilisateur.objects.filter(depart = 'Département des finances').count()
    any =int(any)
    eny = Utilisateur.objects.filter(depart = 'Département des ressources humaines').count()
    eny =int(eny)
    aty = Utilisateur.objects.filter(depart = 'Département des technologies informatiques').count()
    aty =int(aty)
    euy = Utilisateur.objects.filter(depart = 'Département des ventes et du marketing').count()
    euy =int(euy)
    afy = Utilisateur.objects.filter(depart = 'Département des services aux clients').count()
    afy =int(afy)
    genre_list = ['Masculin', 'Féminin']
    nomb_genre_list = [trm, rep]
    nationalité_list = ['Tunisie', 'Algérie', 'Libye', 'Européen', 'Afrique subsaharienne', 'Pays du golf et Moyen orient', 'Autre']
    nomb_nationalité_list = [ann, enc, att, eur, afr, gol, atr]
    type_list = ['Compte jeune', 'Compte chèque','Compte épargne' , 'Compte courant']
    nomb_type_list = [trn, req, an, en]
    etat_list = ['Compte Fermé', 'Compte Bloqué', 'Compte Actif']
    nomb_etat_list = [at, eu, af]
    depart_list = ['Département des opérations bancaires', 'Département des prêts', 'Département des finances', 'Département des ressources humaines', 'Département des technologies informatiques', 'Département des ventes et du marketing', 'Département des services aux clients' ]
    nomb_depart_list = [tr, re, any, eny, aty,euy, afy ]
    context = {
        'client' : client,
        'genre_list' : genre_list,
        'nomb_genre_list' : nomb_genre_list,
        'nationalité_list' : nationalité_list,
        'nomb_nationalité_list' : nomb_nationalité_list,
        'compte' : compte,
        'type_list' : type_list,
        'nomb_type_list' : nomb_type_list,
        'etat_list' : etat_list,
        'nomb_etat_list' : nomb_etat_list,
        'uset': uset,
        'depart_list': depart_list,
        'nomb_depart_list': nomb_depart_list,
    }
    
    return render(request, 'home.html',context)

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Client.csv'
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Prénom', 'Adresse', 'Adresse Mail', 'Numéro Téléphone', 'Genre', 'Nationalité', 'Profession', 'Statut matrimonial', 'Nombre de personne en charge', 'Revenue Annuel', 'Date de Naissance'])
    client = Client.objects.all()
    for client in client:
        writer.writerow([client.nom, client.prenom, client.adresse, client.email, client.num_tel, client.genre, client.nationalité, client.profession, client.statut_mat, client.nbr_per, client.revenue_annuel, client.date_naissance ])
    return response