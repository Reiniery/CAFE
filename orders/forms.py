from django import forms
from menu.models import Product

class OrderForm(forms.Form):
    customer_name= forms.CharField(max_length=100)
    customer_email=forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products= Product.objects.filter(avaialble=True)
        for product in products:
            self.fields[f'prodcut_{product.id}'] = forms.IntegerField(
                label= product.name,
                min_value=0,
                initial=0,
                required = False
            )
        