from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from user.forms import ProfileUpdateForm, RegisterForm
from user.models import UserProfile
from django.views.generic.edit import UpdateView

from about.models import infoCompany
from product.models import website
from help.models import Questions
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator

from about.models import infoCompany 


# Create your views here.

def login_user(request):
    message= ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url

            return redirect('home')
        else:
            print("sai")
            messages.info(request, "Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại")
    
    return render(
        request=request,
        template_name="login.html",
        context={
            'message':message
        }
    )
    

def register_user(request):
    form = RegisterForm()

    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            user = authenticate(username=username, password=password)

            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id=current_user.id
            data.image="images/users/userimg.png"
            request.session['userimage'] = data.image.url
            data.save()
            return redirect('home')
            # messages.success(request, 'Tài khoản của bạn đã tạo thành công!')

        else:
            print('sai')
            messages.info(request, form.errors)
    
    return render(
        request=request,
        template_name= "register.html",
        context={
            'form':form,
        }
    )

@login_required(login_url='/login')
def userPage(request):
    current_user = request.user
    user_profile = UserProfile.objects.get(user_id=current_user.id)
    info = infoCompany.objects.get(pk=1)

    return render(
        request=request,
        template_name='user_page.html',
        context={
            'user_profile': user_profile,
            'info':info
        }
    )

# @method_decorator(login_required, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = UserProfile
#     form_class = ProfileUpdateForm
#     template_name = "update_userpage.html"
#     success_url="/user/userpage/"

@login_required(login_url='/login')
def user_update(request):
    info = infoCompany.objects.get(pk=1)
    if request.method == 'POST':
        # user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            # messages.success(request, 'Tài khoản của bạn đã được cập nhật!')
            return HttpResponseRedirect('/user/userpage/')
    else:
        # user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            'info':info,
            'profile_form': profile_form
        }
    return render(request, 'update_userpage.html', context=context)

