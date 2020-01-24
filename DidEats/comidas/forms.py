from django import forms

from .models import Comida

class ComidaCreateForm(forms.ModelForm):
	"""docstring for ComidaCreateForm"""
	comida_id = forms.CharField(label = "ID", required=True,
					widget = forms.TextInput(
						attrs={
							"placeholder":"Ingrese la id de la comida",
							"minlength":3
						}
					)
				)
	comida_nombre = forms.CharField(label="Nombre Comida", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el nombre de la comida",
                            "minlength":5
                        }
                )   
            )
	comida_valor = forms.IntegerField(label="Precio", required =True,
                    widget=forms.NumberInput(
                        attrs={
                            "placeholder":"Precio Comida"
                        }
                    )
                )
	comida_descripcion = forms.CharField(label="Descripcion", required=True,
                widget=forms.Textarea(
                        attrs={
                            "placeholder":"Ingrese descripcion de la comida",
                            "minlength":5,
                            "maxlength":3000
                        }
                )   
            )
	comida_imagen = forms.ImageField(label="Imagen principal")

	class Meta:
		"""docstring for Meta"""
		model = Comida
		fields = [
			'comida_id',
			'comida_nombre',
			'comida_valor',
			'comida_descripcion',
			'comida_imagen'
		]
			