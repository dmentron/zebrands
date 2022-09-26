# -*- coding: utf-8 -*-
import smtplib

from applications.producto.models import Producto
from applications.usuario.models import NotificacionUsuario

from django.contrib.auth.models import User

def notification(product_id, action):
    all_objects_users = User.objects.all()
    for user in all_objects_users:
        product = Producto.objects.get(id = product_id)

        NotificacionUsuario.objects.create(
            user = user,
            producto = product,
            accion = action
        )   

        # Send mail
        send_mail(user, product)


def send_mail(user, product):
    # print(user.email)
    # print(product.nombre)
    from_message = 'mail de notificación <osvaldo.bustamante.n@gmail.com>'
    to =  'para <%s>' % (user.username)
    subject = 'Correo de notificación'

    body = 'Hola!<br/> <br/> Este es un mail de <b>e-mail</b>  <b>Notificación</b>'
    email = 'From: %s To: %s MIME-Version: 1.0 Content-type: text/html Subject: %s %s' % (from_message, to, subject, body) 

    try: 
        smtp = smtplib.SMTP('localhost') 
        smtp.sendmail(from_message, to, email) 
        print('Correo enviado')
    except: 
        print('Error: el mensaje no pudo enviarse. Compruebe que sendmail se encuentra instalado en su sistema')
    









# noti.ip = socket.gethostbyname(socket.gethostname())
# noti.producto = Producto.objects.ger(id = pk)
# noti.save()
