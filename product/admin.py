from django.contrib import admin
from .models import website, emailBusiness, Checkout, Checkout_email
# Register your models here.
admin.site.register(website)
admin.site.register(emailBusiness)
admin.site.register(Checkout)
admin.site.register(Checkout_email)