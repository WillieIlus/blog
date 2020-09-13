from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.models import Blog


class BlogList(ListView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/list.html'


class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/detail.html'
    count_hit = True


class BlogCreate(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/form.html'


class BlogEdit(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/form.html'
