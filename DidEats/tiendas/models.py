from django.db import models
from django.urls import reverse
# Create your models here.

class Tienda(models.Model):
	"""docstring for Tienda"""
	tienda_id = models.CharField(max_length=10,help_text="Ingrese ID de la Tienda",primary_key=True)
	tienda_nombre = models.CharField(max_length=200, help_text="Ingrese Nombre de la Tienda")
	tienda_comuna = models.CharField(max_length=200, help_text="Ingrese Comuna de la Tienda")
	tienda_direccion = models.CharField(max_length=200, help_text="Ingrese Direccion de la Tienda")
	tienda_descripcion=models.TextField(max_length=3000, help_text="Ingrese la descripcion de la Tienda")
	tienda_imagen=models.ImageField(upload_to="gallery", null=True)

	def __str__(self):
		return self.tienda_nombre

	def get_absolute_url(self):
		"""Return the url to access a detail record for this book."""
		return reverse('tiendas:details', args=[str(self.tienda_id)])
