# Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Utilities
from datetime import datetime

from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


posts = [
    {
        'title': '"sistema Polar"',
        'user': {
            'name': 'Nina Simone',
            'picture': 'https://picsum.photos/id/60/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        #'photo': 'https://fotografias.lasexta.com/clipping/cmsimages01/2019/06/04/3EC08BDA-7BE1-4413-A831-277039B478B9/58.jpg',
        'photo': 'https://picsum.photos/id/800/800/903?grayscale&blur=<2></2>'
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

"""antigua forma de llamar los posts que igual toca reviar el por qué no estaba funcionado de manera correcta 
@login_required #decorador de python que permite user la vista solo a usuarios autenticados 
def list_posts(request):
    List existing posts."""
    #return render(request, 'posts/feed.html', {'posts': posts}) sirve la lista d epost declarada
    #posts=Post.objects.all().order_by('-created')
    #return render(request, 'posts/feed.html', {'posts': posts})"""
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'
    #   import pdb; pdb.set_trace()


'''@login_required
def create_post(request):
    if request.method =='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    return render(
        request=request,
        template_name='posts/create.html',
        context={'form':form,
        'user':request.user,
        'profile':request.user.profile})'''

class PostDetailView(LoginRequiredMixin, DetailView):
    #si nio le enviamos template_name el lo buscarà en un lugar predeterminad 
    #por el nombre de details
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/create.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context