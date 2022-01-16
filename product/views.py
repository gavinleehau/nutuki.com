from django.shortcuts import render, redirect
from .models import website, emailBusiness, Checkout, Checkout_email
from about.models import infoCompany
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def product(request):
  websites = website.objects.all()[0:3]
  info = infoCompany.objects.get(pk=1)

  return render(
    request = request,
    template_name= 'product.html',
    context={
	  'websites': websites,
      'info':info
		}
  )

def checkout(request, website_id):
    web_detail = website.objects.get(id = website_id)
    data = Checkout()

    if request.method == 'POST':
        data.email = request.POST['email']
        data.name = request.POST['name']
        data.phone = request.POST['phone']
        data.message = request.POST['message']
        data.selected_package = web_detail
        data.save()
        return redirect('checkout_success')

    info = infoCompany.objects.get(pk=1)   

    return render(
        request = request,
        template_name='checkout.html',
        context={
            'web_detail': web_detail,
            'info':info
        }
    )

def checkout_success(request):
    # data_checkout = Checkout.objects.get(id = checkout_id)

    return render(
        request=request,
        template_name="checkout_success.html",
        context={
            # 'data_checkout': data_checkout,
        }
    )








def email_business(request):
    email_business = emailBusiness.objects.all()
    info = infoCompany.objects.get(pk=1)

    return render(
        request = request,
        template_name= 'email_business.html',
        context={
            'email_business': email_business,
            'info':info
    }
)

def checkout_email(request, email_id):
    email_detail = emailBusiness.objects.get(id = email_id)
    data = Checkout_email()

    if request.method == 'POST':
        data.name_domain = request.POST['name_domain']
        data.number_of_users = request.POST['number_of_users']
        data.used_time = request.POST['used_time']
        data.selected_email_package = email_detail
        data.save()
        return redirect('checkout_success')

    info = infoCompany.objects.get(pk=1)   

    return render(
        request = request,
        template_name='checkout_email.html',
        context={
            'email_detail': email_detail,
            'info':info
        }
    )

def checkout_success(request):
    # data_checkout = Checkout.objects.get(id = checkout_id)

    return render(
        request=request,
        template_name="checkout_success.html",
        context={
            # 'data_checkout': data_checkout,
        }
    )