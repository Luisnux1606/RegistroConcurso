# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    cedula = models.CharField(max_length=150,null=True,blank=True)
    nombres = models.CharField(max_length=150, null=True,blank=True) #equipo
    apellidos = models.CharField(max_length=150, null=True, blank=False) #dos nombres dos apellidos de cada uno
    nro_fono = models.CharField(max_length=150, null=True,blank=True) #representante
    carrera = models.CharField(max_length=150, null=True,blank=True)
    edad = models.SmallIntegerField(null=True,blank=True) #nivel de ciclo
    mail = models.EmailField(null=True,blank=True) #representante
    estado = models.SmallIntegerField(null=True,blank=True) #para borrar
    def __str__(self):
        return self.nombres+' '+self.apellidos
