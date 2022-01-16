from django.shortcuts import render
from .models import article, InstagramFeeds
from django.core.paginator import Paginator
from .models import CommentForm, Comment
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from about.models import infoCompany


# Create your views here.

# @login_required(login_url="login")
def blogs(request):
	blogs = article.objects.all()
	recentPost = article.objects.all().order_by('-id')[0:4]
	instagram_feeds = InstagramFeeds.objects.all().order_by('-id')[0:6] #up ảnh instagram_feeds trang blog

	new_paginator = Paginator(blogs, per_page = 5) #sô bài mỗi page
	page_number = request.GET.get('page')
	page = new_paginator.get_page(page_number)

	info = infoCompany.objects.get(pk=1)

	search = request.GET.get('search')
	if search:
		blogs = article.objects.filter(title__icontains=search)
		print(blogs)

	return render (
		request=request,
		template_name='blogs.html',
		context = {
			'blogs': blogs,
			'recentPost': recentPost,
			'page':page,
			'new_paginator':new_paginator,
			'page_number': page_number,
			'instagram_feeds': instagram_feeds,
			'info':info
		}
	)

def blogDetail(request, blog_id):
	blogs = article.objects.all().order_by('-id')[0:4]
	blog_detail = article.objects.get(id=blog_id)
	comments = Comment.objects.all()
	form = CommentForm()
	comment_count = Comment.objects.all().count()

	nextpost = article.objects.filter(id__gt=blog_detail.id).order_by ('id').first()
	prevpost = article.objects.filter(id__lt=blog_detail.id).order_by('id').last()

	return render(
		request = request,
		template_name="blog_detail.html",
		context={
			'blogs': blogs,
			'blog_detail':blog_detail,
			'nextpost': nextpost,
			'prevpost': prevpost,
			'comments': comments,
			'form': form,
			'comment_count': comment_count
		}
	)

def addcomment(request,id):
	url = request.META.get('HTTP_REFERER')

	if request.method == 'POST' and request.is_ajax(): 
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = Comment()
			new_comment.subject = form.cleaned_data['subject']
			new_comment.comment = form.cleaned_data['comment']
			new_comment.blog_id=id
			current_user= request.user
			new_comment.user_id=current_user.id
			new_comment.save()
			# return HttpResponseRedirect(url)

			data = {}
			data['list'] = render_to_string('blog_detail.html', context=context, request=request)
			return JsonResponse(data)
		else:
			alert("loi roi")
	


		

	# if request.is_ajax():
	# 	data = {}
	# 	data['list'] = render_to_string('blog_detail.html', context=context, request=request)
	# 	return JsonResponse(data)
		

	return HttpResponseRedirect(url)



