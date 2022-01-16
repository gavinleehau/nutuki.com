from django.shortcuts import render
from about.models import infoCompany
from product.models import website
from help.models import Questions
from .models import Feedback, heroDemo

# Create your views here.

def index(request):
	info = infoCompany.objects.get(pk=1)
	websites = website.objects.all()[0:3]
	questions = Questions.objects.all()
	feedbacks = Feedback.objects.all().order_by('-id')[0:3]
	heros = heroDemo.objects.get(pk=1)

	return render(
		request=request,
		template_name='index.html',
		context={
			'info': info,
			'websites': websites,
			'questions': questions,
			'feedbacks': feedbacks,
			'heros': heros
		}
	)

	



