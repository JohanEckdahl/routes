from django.contrib import admin
from .models import Route, Comment, Boulder



class RouteAdmin(admin.ModelAdmin):
	list_display = ('color', 'wall', 'grade', 'name', 'setter', 'date_set')
	list_filter = ['wall', 'date_set', 'grade']
	#search_fields = ['color', 'wall', 'setter']

class BoulderAdmin(RouteAdmin):
	string = "hi"	

class CommentAdmin(admin.ModelAdmin):
	list_display = ('route', 'username', 'date', 'body')



admin.site.register(Route, RouteAdmin)
admin.site.register(Boulder, BoulderAdmin)
admin.site.register(Comment, CommentAdmin)
