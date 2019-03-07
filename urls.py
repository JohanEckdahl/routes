from django.urls import path
from . import views
from . import tables

app_name='routes'

urlpatterns = [
	path('comments/', views.comments, name = 'comments'),
	path('<int:idn>/comment/', views.comment, name = 'comment'),
	#path('routes/', views.routes, name='routes'),
	path('about/', views.about, name='about'),
	path('analytics/', views.analytics, name='analytics'),
	path('', views.routes, name='index'),
]
