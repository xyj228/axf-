from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from mainApp.models import Cart
from mainApp.views import totalPrice
from orderApp.models import Order, orderGoods


def order_info(request):
    orderid = request.GET.get('orderid')
    order = Order.objects.get(pk=orderid)
    context = {
        'order': order
    }
    return render(request, 'axf/order/order.html', context=context)


def make_order(request):
    uid = request.session.get('u_id')
    order = Order()
    order.o_user_id = uid
    order.o_totalprice = totalPrice(uid)
    order.save()

    carts = Cart.objects.filter(uid_id=uid).filter(is_select=True)
    for cart in carts:
        ordergoods = orderGoods()
        ordergoods.og_order = order
        ordergoods.og_goods = cart.gid
        ordergoods.og_goods_num = cart.g_num
        ordergoods.save()
        cart.delete()

    data = {
        'status': 200,
        'msg': 'ok',
        'orderid': order.id
    }
    return JsonResponse(data=data)
