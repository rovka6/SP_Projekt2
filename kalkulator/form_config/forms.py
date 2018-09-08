from django import forms
from kalkulator.models import Graficna

# class BaseForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(BaseForm,self).__init__(*args,**kwargs)
#         for bound_field in self:
#             if hasattr(bound_field, "field") and bound_field.field.required:
#                 bound_field.field.widget.attrs["required"] = "required"


# class GraficnaForm(BaseForm):
#     class Meta:
#         model = Graficna
#         fields = ["image"]

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()