from django.db import models
from presupuestos.models import Constantes
from proyectos.models import Proyectos

# Create your models here.

class RegistroLeccionesAprendidasPresup(models.Model):

    class areas(models.TextChoices):
        PRESUPUESTO = "PRESUPUESTO"
        OBRA = "OBRA"
    
    area = models.CharField(choices=areas.choices, max_length=40, verbose_name="Área")
    nombre = models.CharField(max_length=200, verbose_name="Nombre de la lección")
    confeciona = models.CharField(max_length=5, verbose_name="Confecciona")
    tema = models.CharField(max_length=200, verbose_name="Tema de la lección")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Leccion aprendida presupuesto"
        verbose_name_plural="Lecciones aprendidas presupuesto"

class RegistroConstantes(models.Model):
    constante = models.CharField(max_length=200)
    valor = models.FloatField(verbose_name="Valor")
    fecha = models.DateField(verbose_name="Fecha")

    class Meta:
        verbose_name="Registro de contantes"
        verbose_name_plural="Registros de constantes"

class RegistroValorProyecto(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, verbose_name = "Proyecto")
    fecha = models.DateField(verbose_name = "Fecha que corresponde")
    precio_proyecto = models.FloatField(verbose_name="Precio del proyecto")

    class Meta:
        verbose_name="Registro de precios de proyecto"
        verbose_name_plural="Registro de precios de proyectos"

    def __str__(self):
        return '{}'.format(self.proyecto)

