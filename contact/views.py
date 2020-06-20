from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
from blog.models import Post, Category
from django.http import HttpResponse, HttpResponseRedirect


def contact(request):
    
    
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            empresa = request.POST.get('empresa', '')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            service = request.POST.get('service', '')
            phone = request.POST.get('phone', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "Balanzas Peru: Nuevo mensaje de contacto",
                "La empresa: {}\n\n De {} <{}>\n\nSoicita el servicio de : {} \n\nNumero de contacto: {} \n\nEscribió:\n\n{}".format(empresa, name, email, service, phone, content),
                "no-contestar@balanzas.pe",
                ["keybroga@balanzas.pe"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    
    return render(request, "contact/contact.html", {'form':contact_form})

    