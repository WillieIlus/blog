from django.views.generic import TemplateView

from blog.models import Blog


class Home(TemplateView):
    model = None
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.all()

        return context

