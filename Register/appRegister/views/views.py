# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..forms.forms import PersonaForm
from django.shortcuts import render,redirect
from ..models import Persona

# Create your views here.

def home(request):
    return render(request,'registro/index.html')

def gracias(request):
    personas = Persona.objects.all()
    context = {'personas': personas}

    return render(request,'registro/persona/gracias.html',context)

def createPersona(request):
    formPersonas = PersonaForm(request.POST or None)


    if formPersonas.is_valid():
        formPersonas.save()
        return redirect(gracias)
    else:
        print(formPersonas.errors)

    return redirect(home)
