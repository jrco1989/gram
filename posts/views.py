# Django
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime
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


@login_required
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
       'profile':request.user.profile})



