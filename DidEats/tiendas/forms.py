from django import forms

from .models import Tienda

class TiendaCreateForm(forms.ModelForm):
	"""docstring for ComidaCreateForm"""
	tienda_id = forms.CharField(label = "ID", required=True,
					widget = forms.TextInput(
						attrs={
							"placeholder":"Ingrese la id de la tienda",
							"minlength":3
						}
					)
				)
	tienda_nombre = forms.CharField(label="Nombre Tienda", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el nombre de la tienda",
                            "minlength":5
                        }
                )   
            )
	tienda_comuna = forms.CharField(label="Comuna Tienda", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el comuna de la tienda",
                            "minlength":5
                        }
                	)	 
                )
	tienda_direccion = forms.CharField(label="Direccion Tienda", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el direccion de la tienda",
                            "minlength":5
                        }
                	)	 
                )
	tienda_descripcion = forms.CharField(label="Descripcion", required=True,
                widget=forms.Textarea(
                        attrs={
                            "placeholder":"Ingrese descripcion de la tienda",
                            "minlength":5,
                            "maxlength":3000
                        }
                )   
            )
	tienda_imagen = forms.ImageField(label="Imagen principal")

	class Meta:
		"""docstring for Meta"""
		model = Tienda
		fields = [
			'tienda_id',
			'tienda_nombre',
			'tienda_comuna',
			'tienda_direccion',
			'tienda_descripcion',
			'tienda_imagen'
		]
			