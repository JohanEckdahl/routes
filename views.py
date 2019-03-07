from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django.views.generic.edit import CreateView
from django.views import generic
from django.utils import timezone
from django.conf import settings

from .models import Route, Boulder, Comment
from .tables import RouteTable
from .forms import CommentForm

from django.db.models import Max
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#from matplotlib.ticker import MaxNLocator




def routes(request):
	table = RouteTable(Route.objects.all(), order_by="-date_set")
	RequestConfig(request, paginate=False, ).configure(table)
	return render(request, 'routes/routes.html', {'table': table})

'''
class IndexView(generic.ListView):
	template_name = 'routes/index.html'
	context_object_name = 'all_routes'
	
	def get_queryset(self):
		types=Route
		set = types.objects.order_by('wall')
		return set
'''

def about(request):
	return render(request, 'routes/about.html')


def analytics(request):
	plot()
	image_path = []
	for name in ["grades", "walls", "setters"]:
		image_path.append(settings.MEDIA_URL + '/routes/images/{}.png'.format(name))
	context = {'image_path' : image_path}
	return render(request, 'routes/analytics.html', context)


def comment(request, idn):
	comments = Comment.objects.filter(route = idn).order_by('-date')
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.route = Route.objects.get(pk = idn)
			comment.date = timezone.now()
			comment.save()
	else:	
		form = CommentForm()
	return render(request, 'routes/comment_form.html', {'comments':comments, 'form':form})

def comments(request):
    comments = Comment.objects.order_by('-date')
    return render(request, 'routes/comment_form.html', {'comments':comments, 'form':form})


#-------------#
#   Helpers   #
#-------------#


colors = ['ORANGE', 'GREEN', 'RED', 'BLUE', 'BLACK', 'WHITE', 'PINK',]



def grades():
	plt.figure()
	graph = "grades"
	y=[]
	x = [i[0] for i in Route.GRADES]
	for s in x:
		y.append(Route.objects.filter(grade=s).count())		
	plt.title('Grade Distribution for Lead Routes')
	plt.xlabel('Grade')
	plt.ylabel('Count')
	plt.bar(x,y)
	image_path = settings.MEDIA_ROOT + '/routes/images/{}.png'.format(graph)
	plt.savefig(image_path, bbox_inches = "tight")
	plt.close("all")

def walls():
	plt.figure()
	graph = "walls"
	y=[]	
	x =[x for x in range(1,16)]
	plt.title('Number of Climbs per Lead Wall')
	plt.xlabel('Wall Number')
	ticks = x
	plt.xticks(ticks)
	plt.ylabel('Count')
	y=[0] * len(x)
	bottom = y
	for color in colors:
		bottom = [sum(r) for r in zip(bottom, y)]
		y=[]		
		for i in x:
			y.append(Route.objects.filter(wall=i, tape = color).count())
		if color == 'WHITE':
			edgecolor = 'black'
		else:
			edgecolor = 'none'
		plt.bar(x, y, color = color, bottom = bottom, edgecolor=edgecolor,)
	image_path = settings.MEDIA_ROOT + '/routes/images/{}.png'.format(graph)
	plt.savefig(image_path, bbox_inches = "tight")
	plt.close("all")
	
def setters():
	plt.figure()
	graph="setters"
	y=[]
	Routes= Route.objects.all()
	x = Routes.values_list('setter', flat=True).distinct()	
	for name in x:
		y.append(Route.objects.filter(setter=name).count())
	plt.xticks(rotation=90)
	plt.title('Routes per Setter')
	plt.ylabel('Count')
	plt.bar(x,y)
	image_path = settings.MEDIA_ROOT + '/routes/images/{}.png'.format(graph)
	plt.savefig(image_path, bbox_inches = "tight")
	plt.close("all")

def plot():
	grades()
	walls()
	setters()

