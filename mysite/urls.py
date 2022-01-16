"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views as home_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.index ),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('help/', include('help.urls')),
    path('blogs/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('user/', include('user.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# muốn in ảnh thì phải chạy cái này và import 'from django.conf.urls.static import static'
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

