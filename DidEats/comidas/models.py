from django.db import models
from django.urls import reverse
# Create your models here.

class Comida(models.Model):
	"""docstring for Comida"""
	comida_id = models.CharField(max_length=10,help_text="Ingrese ID de la comida",primary_key=True)
	comida_nombre = models.CharField(max_length=200, help_text="Ingrese Nombre de la comida")
	comida_valor=models.IntegerField(help_text="Ingrese el precio de la comida (Ej: $ 999 999).")
	comida_descripcion=models.TextField(max_length=3000, help_text="Ingrese la descripcion de la comida")
	comida_imagen=models.ImageField(upload_to="gallery", null=True)

	def __str__(self):
		return self.comida_nombre

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('comidas:details', args=[str(self.comida_id)])
