from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from .models import Prospects
# Create your views here.

def prospect(request):

    if request.method=="POST":
        email=request.POST['email']
        nom=request.POST['nom']
        prenom=request.POST['prenom']
        numero1=request.POST['numero']
        numero2=request.POST['whatsapp']
        lieu=request.POST['lieu']
        sexe=request.POST['sexe']
        filiere=request.POST['filiere']
        diplome=request.POST['diplome']

        if email=="" or nom=="" or prenom=="" or numero1=="" or numero2=="" or lieu=="" or sexe=="" or filiere=="" or diplome=="" :
            messages.info(request,"Vérifié que tous les champs sont bien remplis")
            return render(request,"inscription.html")

        else:
            delegate=Prospects.objects.create(email=email,nom=nom,prenom=prenom,numero1=numero1,numero2=numero2,lieu=lieu,sexe=sexe,filiere=filiere,diplome=diplome)
            delegate.save()
            return redirect('/remerciement/')

    return render(request,'inscription.html')


