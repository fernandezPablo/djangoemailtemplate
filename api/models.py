from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la categoria',
        unique = True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Categorias'


class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la subcategoria'
    )

    def __str__(self):
        return '{}{}'.format(self.categoria.descripcion, self.descripcion)

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria','descripcion')

class Producto(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion del producto',
        unique = True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default = False)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Productos'

