from django.core.mail import send_mail

from django.template import loader


def sendEmail(name, email, token):
    index = loader.get_template('axf/user/active.html')

    context = {
        'name': name,
        'url': 'http://101.132.145.202:8000/userapp/account/?token=' + str(token)
    }

    index_value = index.render(context)

    subject = '水上人间开业酬宾'
    html_message = index_value
    from_email = '1021812297@qq.com'
    recipient_list = [email]
    send_mail(subject=subject, message='', html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)
