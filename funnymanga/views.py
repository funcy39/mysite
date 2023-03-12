from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Picture, Comment
from django.utils import timezone
import datetime
# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'funnymanga/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Picture.objects.order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Picture
#     template_name = 'funnymanga/detail.html'

def index(request):
    latest_picture_list = Picture.objects.order_by('-pub_date')[:5]
    context = {'latest_picture_list':latest_picture_list}
    return render(request, 'funnymanga/index.html', context)

def detail(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    context = {'picture': picture}
    return render(request, 'funnymanga/detail.html', context)

def comment(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id)
    picture.comment_set.create(picture=picture, comment_text=request.POST['comment'])
    c = picture.comment_set.filter(comment_text=request.POST['comment'])
    if c is None:
        c.delete()
        raise Exception
    picture.comments += 1
    picture.save()
    return HttpResponseRedirect(reverse('funnymanga:detail', args=(picture_id,)))