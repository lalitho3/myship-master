from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Post
from .forms import UploadPostForm
from django.urls import reverse_lazy

class Index(ListView):
    model = Post
    template_name = 'main/index.html'
    paginate_by: int = 10

    def get_context_object_name(self, object_list):
        return 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My relationship | Inicio'
        return context

class UploadPost(FormView):
    template_name = 'main/upload_post.html'
    form_class = UploadPostForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My relationship | Subir recuerdo'
        return context

    
