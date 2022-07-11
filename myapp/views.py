from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
DetailView,
CreateView,
UpdateView,
DeleteView,
)
from . forms import SubscibersForm
from newsletter.models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from .models import News



def index(request):
    return render(request, 'letter/index.html')

def admission(request):
    return render(request, 'letter/admission.html')

def events(request):
    return render(request, 'letter/events.html')

def news(request):
    if request.method  == 'POST':
        form = SubscibersForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Message Successful!')
            return redirect('news')
    else:
        form = SubscibersForm()
    context = {
        
        'form':form,
        'news': News.objects.all()
    }
    return render(request, 'letter/news.html', context)



class NewsListView(ListView):
    model = News
    template_name = 'letter/news.html'
    context_object_name = 'news'
    ordering = ['-date_posted']
    paginate_by = 2


class NewsDetailView(DetailView):
    model = News

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




    
