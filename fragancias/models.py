from django.db import models


class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True,editable=False)
    disponible = models.BooleanField(default=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'producto'