from django.urls import path 
from posts import views
urlpatterns=[

	path(route='',
		view= views.PostsFeedView.as_view(), 
		name='feed'),
	path(route='post/new/',
		view=views.create_post,
		name='poncha'),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )		
]
