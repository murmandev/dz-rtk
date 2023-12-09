from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Article


class Index(ListView):
    model = Article
    queryset = Article.objects.filter(featured = True).order_by('-date')
    template_name = 'core/index.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_bar_color']= 'index'
        return context


class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured = False).order_by('-date')
    template_name = 'core/featured.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_bar_color']= 'featured'
        return context


class DetailArticleView(DetailView):
    model = Article
    template_name = 'core/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['like_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['like_by_user'] = True 
        return context


class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        
        article.save()
        return redirect('detail_article', pk)


class Moderated(View):

    def post(self, request, pk):

        article = Article.objects.get(id=pk)
        article.featured = True

        article.save()
        return redirect('featured')

   
    
class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'core/create.html'
    fields =['title', 'content', 'image', ]
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav_bar_color']= 'new'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)   
   

    

class DeleteArticleView(DeleteView):
	model = Article
	template_name = 'core/delete.html'
	success_url = reverse_lazy('index')
     

