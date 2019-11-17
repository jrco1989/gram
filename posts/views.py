# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime


posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Nina simone',
            'picture': 'https://ichef.bbci.co.uk/news/660/cpsprodpb/14AAC/production/_105225648_1-1.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        #'photo': 'https://fotografias.lasexta.com/clipping/cmsimages01/2019/06/04/3EC08BDA-7BE1-4413-A831-277039B478B9/58.jpg',
        'photo': 'https://picsum.photos/60/60/?image=1005'
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
@login_required #decorador de python que permite user la vista solo a usuarios autenticados 
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})


