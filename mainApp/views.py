from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from mainApp.models import Wheel, Nav, MustBuy, MainShow, FoodType, Goods, Cart
from userApp.models import User


def home(request):
    wheels = Wheel.objects.all()
    nav = Nav.objects.all()
    mustbuy = MustBuy.objects.all()
    mainshow = MainShow.objects.all()
    context = {
        'wheel': wheels,
        'nav': nav,
        'mustbuy': mustbuy,
        'mainshow': mainshow
    }
    return render(request, 'axf/main/home/home.html', context=context)


def market(request):
    # 左导航栏
    foodtypes = FoodType.objects.all()
    # 获取typeid
    typeid = request.GET.get('typeid', '104749')

    # 获取foodtype中的子类
    foodstype_list = FoodType.objects.get(typeid=typeid)
    childtype_list = []
    for foodtype in foodstype_list.childtypenames.split('#'):
        a = {}
        a['childname'], a['childid'] = foodtype.split(':')
        childtype_list.append(a)
    # 获取childid
    childid = request.GET.get('childtypeid', '0')

    # 获取排序类别
    sort = request.GET.get('sort', '5')

    # 一级查询
    goods_list = Goods.objects.filter(categoryid=typeid)

    # 二级查询
    if childid == None:
        pass
    elif childid == '0':
        pass
    else:
        goods_list = goods_list.filter(childcid=childid)

    # 实现排序
    if sort == '1':
        goods_list = goods_list.order_by('price')
    elif sort == '2':
        goods_list = goods_list.order_by('-price')
    elif sort == '3':
        goods_list = goods_list.order_by('productnum')
    elif sort == '4':
        goods_list = goods_list.order_by('-productnum')
    elif sort == '5':
        goods_list = goods_list.order_by('price').order_by('productnum')
    else:
        pass

    order_list = [['综合查询', '5'], ['价格升序', '1'], ['价格降序', '2'], ['销量升序', '3'], ['销量降序', '4']]

    context = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'childid': childid,
        'sort': sort,
        'childtype_list': childtype_list,
        'order_list': order_list

    }
    return render(request, 'axf/main/market/market.html', context=context)


def cart(request):
    uid = request.session.get('u_id')
    carts = Cart.objects.filter(uid_id=uid)
    is_all_select = not carts.filter(is_select=False).exists()
    context = {
        'carts': carts,
        'is_all_select': is_all_select,
        'totalprice': totalPrice(uid)
    }

    return render(request, 'axf/main/cart/cart.html', context=context)


def mine(request):
    u_id = request.session.get('u_id')

    if u_id:
        user = User.objects.get(pk=u_id)
        context = {
            'user1': user
        }
        return render(request, 'axf/main/mine/mine.html', context=context)
    else:
        return render(request, 'axf/main/mine/mine.html')


# 闪购goods增加
def addCart(request):
    uid = request.session.get('u_id')
    if uid:
        gid = request.GET.get('gid')
        carts = Cart.objects.filter(gid_id=gid).filter(uid_id=uid)
        if carts.exists():
            cart = carts[0]
            cart.g_num += 1
        else:
            cart = Cart(uid_id=uid, gid_id=gid)
        cart.save()
        data = {
            'status': 200,
            'msg': 'ok',
            'g_num': cart.g_num
        }
        return JsonResponse(data=data)
    else:
        return redirect(reverse('userapp:login'))


# 闪购goods减少
def subCart(request):
    uid = request.session.get('u_id')
    if uid:
        gid = request.GET.get('gid')
        carts = Cart.objects.filter(uid_id=uid).filter(gid_id=gid)
        if carts.exists():
            cart = carts[0]
            cart.g_num -= 1
        else:
            cart = Cart()
            cart.gid = gid
            cart.uid = uid
        cart.save()
        data = {
            'status': 200,
            'msg': 'ok',
            'g_num': cart.g_num
        }
        return JsonResponse(data=data)
    else:
        return redirect(reverse('userapp:login'))


# 修改购物车单选框状态
def changeSingle(request):
    cart_id = request.POST.get('cid')
    print(cart_id)
    ca = Cart.objects.get(pk=cart_id)
    ca.is_select = not ca.is_select
    ca.save()

    uid = request.session.get('u_id')
    is_all_select = not Cart.objects.filter(uid_id=uid).filter(is_select=False).exists()
    data = {
        'status': 200,
        'msg': 'success',
        'is_select': ca.is_select,
        'is_all_select': is_all_select,
        'totalprice': totalPrice(uid)
    }
    return JsonResponse(data=data)


# 修改购物车全选框状态
def allSelect(request):
    cart_list = request.GET.get('cart_list')
    cid = cart_list.split('#')
    carts = Cart.objects.filter(pk__in=cid)
    for cart in carts:
        cart.is_select = not cart.is_select
        cart.save()

    data = {
        'status': 200,
        'msg': 'ok',
        'totalprice': totalPrice(request.session.get("u_id"))
    }

    return JsonResponse(data=data)


# 购物车减
def sub(request):
    cid = request.GET.get('cid')
    cart = Cart.objects.get(pk=cid)
    data = {
        'status': 200,
        'msg': 'ok',
    }
    if cart.g_num > 1:
        cart.g_num -= 1
        cart.save()
        data['g_num'] = cart.g_num
    else:
        cart.delete()
    data['totalprice'] = totalPrice(request.session.get('u_id'))
    return JsonResponse(data=data)


# 购物车加
def add(request):
    cid = request.POST.get('cid')
    cart = Cart.objects.get(pk=cid)
    cart.g_num += 1
    cart.save()
    data = {
        'status': 200,
        'msg': 'ok',
        'g_num': cart.g_num,
        'totalprice': totalPrice(request.session.get('u_id'))
    }
    print(data)
    return JsonResponse(data=data)


# 购物车总价
def totalPrice(uid):
    carts = Cart.objects.filter(uid_id=uid).filter(is_select=True)
    totalprice = 0
    for cart in carts:
        price = cart.gid.price
        totalprice = totalprice + price * cart.g_num
    return ('%.2f' % totalprice)
