from django.db import models
from proyectos.models import Proyectos

# Create your models here.

class PricingResumen(models.Model):
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, verbose_name = "Proyecto")
    fecha = models.DateField(verbose_name = "Fecha que corresponde")
    precio_prom_contado = models.FloatField(verbose_name="Precio promedio contado")
    precio_prom_financiado = models.FloatField(verbose_name="Precio promedio financiado")
    anticipo = models.FloatField(verbose_name="Anticipo")
    cuotas_pend = models.IntegerField(verbose_name="Cuotas pendientes") 

    class Meta:
        verbose_name="Resumen de pricing"
        verbose_name_plural="Resumen de pricing"

    def __str__(self):
        return '{}'.format(self.proyecto)

class VentasRealizadas(models.Model):

    class ModoVenda(models.TextChoices):
        VENTA = "VENTA"
        CANJE = "CANJE"

    class TipoUnidad(models.TextChoices):
        DTO = "DTO"
        COCHERA = "COCHERA"

    comprador = models.CharField(max_length=100, verbose_name="Nombre del comprador")
    fecha = models.DateField(verbose_name = "Fecha de venta")
    tipo_venta = models.CharField(choices=ModoVenda.choices, max_length=20, verbose_name="Tipo de venta", blank=True, null=True)
    unidad = models.CharField(max_length=100, verbose_name="Unidad")
    tipo_unidad = models.CharField(choices=TipoUnidad.choices, max_length=20, verbose_name="Tipo de unidad", blank=True, null=True)
    proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, verbose_name = "Proyecto")
    asignacion = models.CharField(max_length=100, verbose_name="Asignacion")   
    m2 = models.FloatField(verbose_name="Metros cuadrados")
    precio_venta = models.FloatField(verbose_name="Precio de venta")
    anticipo = models.FloatField(verbose_name="Anticipo")
    cuotas_pend = models.IntegerField(verbose_name="Cuotas pendientes") 

    class Meta:
        verbose_name="Venta"
        verbose_name_plural="Ventas"

    def __str__(self):
        return '{}'.format(self.proyecto)

class EstudioMercado(models.Model):
    fecha = models.DateField(verbose_name="Fecha del estudio")
    zona = models.CharField(max_length=100, verbose_name="Zona del estudio")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    proyecto = models.CharField(max_length=100, verbose_name="Nombre del proyecto")
    meses = models.IntegerField(verbose_name="Meses a la entrega")
    precio = models.FloatField(verbose_name="Precio")

    class Meta:
        verbose_name="Estudio de mercado"
        verbose_name_plural="Estudios de mercado"

    def __str__(self):
        return self.empresa
