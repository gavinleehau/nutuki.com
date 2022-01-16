from django.shortcuts import render, redirect
from .models import contact
from about.models import infoCompany
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def contact_view(request):
    data = contact()
    if request.method == 'POST':
        data.email = request.POST['email']
        data.name = request.POST['name']
        data.phone = request.POST['phone']
        data.subject = request.POST['subject']
        data.message = request.POST['message']
        data.save()
        return redirect('success_page')

    info = infoCompany.objects.get(pk=1)   

    return render(
        request = request,
        template_name='contact.html',
        context={
            'info':info
        }
    )

def success_page(request):
    data_contact = contact.objects.all().order_by('-id')[0:1]
    print(data_contact)
    return render(
        request=request,
        template_name="success_page.html",
        context={
            'data_contact': data_contact,
        }
    )
