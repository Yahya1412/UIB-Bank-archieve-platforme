from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.shortcuts import redirect
from .models import  Compte, Type, Etat
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse
import csv
from datetime import datetime

@login_required(login_url='/authent/login/')
def index(request):
    etat = Etat.objects.all()
    type = Type.objects.all()
    comptes = Compte.objects.order_by('owner')
    paginator = Paginator(comptes,7)
    page_number=request.GET.get('page')
    page_obj=Paginator.get_page(paginator, page_number)
    context={
        'comptes': comptes,
        'etat': etat,
        'type': type,
        'page_obj': page_obj,
    }
    return render(request, 'compte/index.html', context)
@login_required(login_url='/authent/login/')

def ajouter_tache(request):
    etat = Etat.objects.all()
    type = Type.objects.all()
    comptes = Compte.objects.all()

    context = {
        'comptes': comptes,
        'etat': etat,
        'type': type,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'compte/ajouter_compte.html', context)

    if request.method == 'POST':
        rib = request.POST['rib']
        if not rib:
            messages.warning(request, 'Le champ ID est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)

        owner = request.POST['owner']
        if not owner:
            messages.warning(request, 'Le champ Propriétaire est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)

        type = request.POST['type']
        if not type:
            messages.warning(request, 'Le champ Type de compte est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)
        num_compte = request.POST['num_compte']
        if not num_compte:
            messages.warning(request, 'Le champ Numéro de compte est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)
        solde = request.POST['solde']
        if not solde:
            messages.warning(request, 'Le champ Solde du compte est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)

        etat = request.POST['etat']
        if not etat:
            messages.warning(request, 'Le champ Etat de compte est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)

        date_debut = request.POST['date_debut']
        if not date_debut:
            messages.warning(request, 'Le champ Date ouverture du compte est nécessaire')
            return render(request, 'compte/ajouter_compte.html', context)

        

        Compte.objects.create(
            rib=rib,
            owner=owner,
            type=type,
            num_compte=num_compte,
            solde=solde,
            etat=etat,
            date_debut=date_debut,
        )

        messages.success(request, 'Compte enregistrée avec succès')
        return redirect('compte')


@login_required(login_url='/authent/login/')


def tache_edit(request, id):
    compte = Compte.objects.get(pk=id)
    etat = Etat.objects.all()
    type = Type.objects.all()
    context ={
        'compte' : compte,
        'values' : compte,
        'etat': etat,
        'type': type,
    }

    if request.method == 'GET':
        return render(request, 'compte/modifier_compte.html', context)

    if request.method == 'POST':
        rib = request.POST['rib']
        if not rib:
            messages.warning(request, 'Le champ Identifiant du Compte est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)

        owner = request.POST['owner']
        if not owner:
            messages.warning(request, 'Le champ Propriétaire est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)

        type = request.POST['type']
        if not type:
            messages.warning(request, 'Le champ Type de compte est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)
        num_compte = request.POST['num_compte']
        if not num_compte:
            messages.warning(request, 'Le champ Numéro de compte est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)
        solde = request.POST['solde']
        if not solde:
            messages.warning(request, 'Le champ Solde du compte est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)

        etat = request.POST['etat']
        if not etat:
            messages.warning(request, 'Le champ Etat de compte est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)

        date_debut = request.POST['date_debut']
        if not date_debut:
            messages.warning(request, 'Le champ Date ouverture du compte est nécessaire')
            return render(request, 'compte/modifier_compte.html', context)

        compte.rib = rib
        compte.owner = owner
        compte.type = type
        compte.num_compte= num_compte
        compte.solde = solde
        compte.etat = etat
        compte.date_debut = date_debut
        compte.save()

        messages.success(request, 'Modification enregistrée avec succès')
        return redirect('compte')

@login_required(login_url='/authent/login/')
def supprimer_tache(request, id):
    compte = Compte.objects.get(pk=id)
    compte.delete()
    messages.success(request,'Compte supprimer avec succés')
    return redirect('compte')
@login_required(login_url='/authent/login/')
def stats_compte(request):
    compte = Compte.objects.all()
    trm = Compte.objects.filter(genre = 'Compte jeune').count()
    trm =int(trm)
    rep = Compte.objects.filter(genre = 'Compte chèque').count()
    rep =int(rep)
    ann = Compte.objects.filter(nationalité = 'Compte épargne').count()
    ann =int(ann)
    enc = Compte.objects.filter(nationalité = 'Compte courant').count()
    enc =int(enc)
    att = Compte.objects.filter(nationalité = 'Compte Fermé').count()
    att =int(att)
    eur = Compte.objects.filter(nationalité = 'Compte Bloqué').count()
    eur =int(eur)
    afr = Compte.objects.filter(nationalité = 'Compte Actif').count()
    afr =int(afr)
    type_list = ['Compte jeune', 'Compte chèque','Compte épargne' , 'Compte courant']
    nomb_type_list = [trm, rep, att, enc]
    etat_list = ['Compte Fermé', 'Compte Bloqué', 'Compte Actif']
    nomb_etat_list = [att, eur, afr]
    context = {
        'compte' : compte,
        'type_list' : type_list,
        'nomb_type_list' : nomb_type_list,
        'etat_list' : etat_list,
        'nomb_etat_list' : nomb_etat_list,
    }
    return render(request, 'home.html',context)

def export_csv_compte(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Compte.csv'
    writer = csv.writer(response)
    writer.writerow(['Nom du propriétaire', 'Type du compte', 'Numéro du compte', 'Solde du compte', 'Etat du compte', 'Date début'])
    compte = Compte.objects.all()
    for compte in compte:
        writer.writerow([compte.owner, compte.type, compte.num_compte, compte.solde, compte.etat,compte.date_debut])
    return response