from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from .models import Prospects
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage
from templated_email import send_templated_mail

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
        naissance=request.POST['naissance']


        if email=="" or nom=="" or prenom=="" or numero1=="" or numero2=="" or lieu=="" or sexe=="" or filiere=="" or diplome=="" or naissance=="":
            messages.info(request,"Tous les champs sont obligatoires")
            return render(request,"inscription.html")

        else:
            # Send mail
            boite=send_templated_mail(
                subject="Merci pour votre inscription",
                template_name='mail',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                context={
                'nom':nom,
                'prenom':prenom
                },
)
            # Create prospect

            delegate=Prospects.objects.create(email=email,nom=nom,prenom=prenom,numero1=numero1,numero2=numero2,lieu=lieu,sexe=sexe,filiere=filiere,diplome=diplome,date=naissance)
            delegate.save()


            return redirect('/remerciement/')

    return render(request,'inscription.html')


def test(request):
    return render(request,"mail.html")

