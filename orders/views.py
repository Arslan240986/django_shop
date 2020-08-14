from django.contrib.admin.views.decorators import staff_member_required
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            #Ochishayem korzinu
            cart.clear()

            # Zapusk asinhronnoy zadachi.
            order_created.delay(order.id,)
            # order_created.delay(order.id)
            return render(request,
                          'order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm(auto_id=False)
        return render(request,
                      'order/create.html',
                      {'cart': cart, 'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    print('this is view: {}'.format(order_id))
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/admin_order_detail.html',
                  {'order': order})