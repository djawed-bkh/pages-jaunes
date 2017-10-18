from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from entreprises.models import Entreprise
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def index(request):
    entr=Entreprise.objects.all()
    entrs = {'entreprises':entr,'test':'fgfgfgfgfg'}
    return render(request,'doss.html',entrs)
   
def detail(request,entreprises_id):
    enter=get_object_or_404(Entreprise,id=entreprises_id)
    dicti={'entreprise':enter} 
    return render(request,'details.html',dicti)
def recherche(request):
    recherche=request.GET.get('valeur','')
    rec=Entreprise.objects.filter(nom__icontains=recherche)
    print(recherche)
    return render(request,'recherche.html',{'entreprises':rec})
def inscription(request):
    if (request.method=="POST"):
        nom=request.POST.get('nom',"")
        prenom=request.POST.get('prenom',"")
        mail=request.POST.get('mail',"")
        pasword=request.POST.get('pasword',"")
        cherche = User.objects.filter(email=mail)
        if(len(cherche)==0):
            utilisateur=User.objects.create(first_name=prenom,last_name=nom,email=mail,password=make_password(pasword),username=mail.split('@')[0])
        print(cherche)
        return HttpResponse("reussi")
    print(request.method)
    return HttpResponse("ca marche")
def conexion(request):
    return render(request,'doss.html',{})
def infos(request):
    return render(request,'infos.html',{})
# Create your views here.
