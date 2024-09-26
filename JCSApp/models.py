from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Campo de texto con un límite de 100 caracteres
    descripcion = models.TextField()  # Campo de texto largo para descripción
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para precio con 2 decimales
    disponible = models.BooleanField(default=True)  # Campo para disponibilidad
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha automática de creación

    def __str__(self):
        return self.nombre  # Retorna el nombre del producto como representación del objeto

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']  # Ordena por fecha de creación de forma descendente
