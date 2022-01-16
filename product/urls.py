from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.product, name='product' ),
    path('email_business/',views.email_business, name='email_business' ),
    re_path(r"^checkout/(?P<website_id>[0-9]+)$",views.checkout, name='checkout' ),
    re_path(r"^success/$",views.checkout_success, name='checkout_success' ),

    re_path(r"^checkout_email/(?P<email_id>[0-9]+)$",views.checkout_email, name='checkout_email' ),
    re_path(r"^success/$",views.checkout_success, name='checkout_success' ),
]