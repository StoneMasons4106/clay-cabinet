from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    image_two = forms.ImageField(label='Image Two', required=False, widget=CustomClearableFileInput)
    image_three = forms.ImageField(label='Image Three', required=False, widget=CustomClearableFileInput)
    image_four = forms.ImageField(label='Image Four', required=False, widget=CustomClearableFileInput)
    image_five = forms.ImageField(label='Image Five', required=False, widget=CustomClearableFileInput)
    image_six = forms.ImageField(label='Image Six', required=False, widget=CustomClearableFileInput)
    image_seven = forms.ImageField(label='Image Seven', required=False, widget=CustomClearableFileInput)
    image_eight = forms.ImageField(label='Image Eight', required=False, widget=CustomClearableFileInput)
    image_nine = forms.ImageField(label='Image Nine', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'