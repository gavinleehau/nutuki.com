from django.shortcuts import render
from .models import Questions
from about.models import infoCompany

# Create your views here.

def help(request):
  questions = Questions.objects.all()
  info = infoCompany.objects.get(pk=1)

  return render(
    request=request,
    template_name='help.html',
    context={
      'questions': questions,
      'info':info
    }
  )