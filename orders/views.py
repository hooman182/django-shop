from django.shortcuts import render
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from orders.tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            #launch asynchronous task
            order_created.delay(order.id)
            return render(request, 'orders/order_success.html', {'order': order})
    else:
        order_form = OrderCreateForm()
            
    return render(request, 'orders/order_create.html', {'cart': cart, 'order_form': order_form})
