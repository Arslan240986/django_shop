from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem


@task
def order_created(order_id):
    product = OrderItem.objects.get()
    print('this is :{}'.format(product))
    """ Zadacha otpravki email-uvedomleniy pri uspeshnom oformlenii zakaza."""
    order = Order.objects.get(id=order_id)

    subject = 'Zakazynyzyn belligi nr. {}'.format(order_id)
    message = 'Gadyrly {},\n\nSizin shu ashakdaky satyn alan ady: {}, bahasy: {}, sanay: {}, \n\nSizin satyn almak uchin eden onumleriniz bellige alyndy .' \
              '\nSizin zakazynyzyn belligi {}.'.format(order.first_name, product.product, product.price, product.quantity, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'oydencom@gmail.com',
                          [order.email])
    return mail_sent