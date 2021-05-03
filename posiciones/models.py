from django.db import models

# Create your models here.


class TipoDePuesto(models.Model):
    id = models.AutoField(primary_key=True)
    cnombre = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, null=True)
    

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    cnombre = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, null=True)


class Idioma(models.Model):
    id = models.AutoField(primary_key=True)
    INGLES = 'IN'
    IDIOMAS_CHOICES = [
        (INGLES, 'Ingles')
    ]
    chidioma = models.CharField(
        max_length=2,
        choices=IDIOMAS_CHOICES,
        default=INGLES,
    )
    BASICO = 'BA'
    INTERMEDIO = 'IN'
    AVANZADO = 'AV'
    FLUIDO = 'FL'
    NIVEL_CHOICES = [
        (BASICO, 'Basico'),
        (INTERMEDIO, 'Intermedio'),
        (AVANZADO, 'Avanzado'),
        (FLUIDO, 'Fluido'),
    ]
    chnivel = models.CharField(
        max_length=2,
        choices=NIVEL_CHOICES,
        default=BASICO,
    )
    BASICO = 'BA'
    INTERMEDIO = 'IN'
    AVANZADO = 'AV'
    FLUIDO = 'FL'
    NIVEL_CHOICES = [
        (BASICO, 'Basico'),
        (INTERMEDIO, 'Intermedio'),
        (AVANZADO, 'Avanzado'),
        (FLUIDO, 'Fluido'),
    ]
    chnivel = models.CharField(
        max_length=2,
        choices=NIVEL_CHOICES,
        default=BASICO,
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, null=True)


class Posicion(models.Model):
    id = models.AutoField(primary_key=True)
    itipoDePuesto = models.ForeignKey(
        TipoDePuesto, null=True, on_delete=models.CASCADE
    )
    iidioma = models.ForeignKey(
        Idioma, null=True, on_delete=models.CASCADE
    )
    icategoria = models.ForeignKey(
        Categoria, null=True, on_delete=models.CASCADE
    )
    PRIMARIA = 'PR'
    SECUNDARIA = 'SC'
    PREPARATORIA = 'PP'
    UNIVERSIDAD = 'UV'
    MAESTRIA = 'MA'
    ESCOLARIDAD_CHOICES = [
        (PRIMARIA, 'Primaria'),
        (SECUNDARIA, 'Secundaria'),
        (PREPARATORIA, 'Preparatoria'),
        (UNIVERSIDAD, 'Universidad'),
        (MAESTRIA, 'Maestria'),
    ]
    chescolaridad = models.CharField(
        max_length=2,
        choices=ESCOLARIDAD_CHOICES,
        default=PRIMARIA,
    )
    iexperiencia = models.IntegerField()
    fsalario = models.FloatField()
    chabilidadesRequeridas = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now_add=True, null=True)


