from django.urls import path 
from posts import views
from django.views.generic import TemplateView
urlpatterns=[

	path(route='',
		view= views.PostsFeedView.as_view(), 
		name='feed'),
	
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
	path(route='post/new/',
		view=views.CreatePostView.as_view(),
		name='poncha'),
	path(route='post/featured/',
		view=TemplateView.as_view(template_name='posts/featured.html'),
		name="featured"
		),
]
