from django.shortcuts import render
from .forms import OrderForm
from .models import Order, OrderItem
from menu.models import Product
# Create your views here.

def order_view(request):
    available_products = Product.objects.filter(available=True)

    if not available_products.exists():
        return render(request, 'orders/no_products.html')

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order =Order.objects.create(
                customer_name = form.cleaned_data['customer_name'],
                customer_email= form.cleaned_data['customer_email']
            )
            for product in Product.objects.filter(available=True):
                qty = form.cleaned_data.get(f'product_{product.id}')
                if qty and qty>0:
                    OrderItem.objects.create(order=order, product=product, quantity=qty)
            return render(request,'orders/order_success.html', {'order',order})
        
        else:
            form=OrderForm()

        return render(request, 'orders/order_form.html', {'form':form})


