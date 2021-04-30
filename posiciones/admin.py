from django.contrib import admin
from .models import Posicion, TipoDePuesto, Idioma

# Register your models here.
admin.site.register(Posicion)
admin.site.register(TipoDePuesto)
admin.site.register(Idioma)