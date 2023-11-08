from django.db import models
from django.utils import timezone
import datetime
    
class Users(models.Model):
    email = models.CharField(max_length=100, null = False)  # Campo para almacenar la dirección de correo electrónico del usuario
    contraseña = models.CharField(max_length=250, null = False)  # Campo para almacenar la contraseña del usuario (debes almacenarla de forma segura, como un hash)
    status = models.BooleanField(default=True, null = True)  # Campo booleano que puede ser nulo (NULL en la base de datos)
    created_at = models.DateTimeField(default=datetime.datetime.now, null = False)  # Campo para almacenar la fecha y hora de creación (no puede ser nulo)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null = False)  # Campo para almacenar la fecha y hora de actualización (no puede ser nulo)
    delete_at = models.DateTimeField(null=True)  # Campo para almacenar la fecha y hora de eliminación, que puede ser nulo


class Identificacion_Types(models.Model):
   
    name = models.CharField(max_length=50, null = False)  # Campo para almacenar el nombre, NOT NULL en la base de datos
    abrev = models.CharField(max_length=10, null = False)  # Campo para almacenar la abreviatura, NOT NULL en la base de datos
    descrip = models.CharField(max_length=100, null = False)  # Campo para almacenar la descripción, NOT NULL en la base de datos
    created_at = models.DateTimeField(default=datetime.datetime.now, null = False)  # Campo para almacenar la fecha y hora de creación (no puede ser nulo)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null = False)  # Campo para almacenar la fecha y hora de actualización (no puede ser nulo)
    






