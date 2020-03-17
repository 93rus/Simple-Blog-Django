from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from django.urls import reverse

from .models import Article, Comment
def index(request):
	lates_article_list = Article.objects.order_by('-pub_date')[:5]
	return render(request, 'articales/list.html', {'lates_article_list': lates_article_list})

def detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена")

	lates_comments_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'articales/detail.html', {'article' : a, 'lates_comments_list': lates_comments_list} )

def  leave_comment(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена")		
	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])	

	return HttpResponseRedirect(reverse('articales:detail', args=(a.id, )))