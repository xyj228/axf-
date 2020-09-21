import uuid
from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from axf import settings
from userApp.models import User
from userApp.views_help import sendEmail


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        icons = request.FILES.get('icons')
        get_token = uuid.uuid4()

        user = User(name=name, email=email, password=password, icon=icons, token=get_token)
        user.save()

        sendEmail(name, email, get_token)

        cache.set(get_token, user.id, timeout=60)

        return redirect(reverse('userapp:login'))
    return render(request, 'axf/user/register.html')


def check_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            User.objects.get(name=name)
        except Exception:
            context = {
                'flag': True,
                'msg': '用户名可用'
            }
        else:
            context = {
                'flag': False,
                'msg': '该用户名已注册'
            }
        return JsonResponse(context)


# def sendemail(request):
#     subject = '12'
#     message = 'success'
#     from_email = '1021812297@qq.com'
#     recipient_list = ['1021812297@qq.com']
#     send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
#
#     return HttpResponse('cheng')


def account(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
    if user_id:

        user = User.objects.get(pk=user_id)

        user.active = True

        user.save()

        cache.delete(token)

        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件过期，请重新激活')


def login(request):
    if request.method == 'POST':
        icode = request.POST.get('icode')
        verify_code = request.session.get('verify_code')
        if icode.lower() == verify_code.lower():
            name = request.POST.get('name')
            user = User.objects.filter(name=name)
            if user.count() != 0:
                password = request.POST.get('password')
                u = user[0]
                if u.password == password:
                    if u.active == True:
                        request.session['u_id'] = u.id
                        return redirect(reverse('mainapp:mine'))
                    else:
                        context = {
                            'msg': '用户未激活，请先激活再登录'
                        }
                        return render(request, 'axf/user/login.html', context=context)
                else:
                    context = {
                        'msg': '用户名或密码错误'
                    }
                    return render(request, 'axf/user/login.html', context=context)
            else:
                context = {
                    'msg': '用户名或密码错误'
                }
                return render(request, 'axf/user/login.html', context=context)
        else:
            context = {
                'msg': '验证码错误'
            }
            return render(request, 'axf/user/login.html', context=context)
    else:
        return render(request, 'axf/user/login.html')


def logout(request):
    request.session.flush()
    return redirect(reverse('mainapp:mine'))


def get_code(request):
    # 初始化画布，初始化画笔
    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(1000):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(200), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = ""
    for i in range(4):
        code += random.choice(source)
    return code
