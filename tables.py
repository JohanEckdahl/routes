import django_tables2 as tables
from .models import Route


comment = '''<a href="{{record.id}}/comment" class="btn btn-default glyphicon glyphicon-comment">&nbsp{{record.comment_count}}</a>'''

grade = '{{record.grade}}&nbsp{% if record.grade|length < 2 %}&nbsp&nbsp{% endif %}{% if record.grade|length < 3 %}&nbsp&nbsp{% endif %}<span class="glyphicon glyphicon-minus" style="color:{% firstof record.tape "transparent" %}"></span>'

date_set = '{{record.date_set|date:"d M Y"}}&nbsp{% if record.coming_down %} <span class="glyphicon glyphicon-hourglass" style="color:red"></span>{% endif %}'

class RouteTable(tables.Table):
	comment = tables.TemplateColumn(comment, orderable=False, verbose_name='Comments')
	grade = tables.TemplateColumn(grade)
	date_set = tables.TemplateColumn(date_set)
	class Meta:
		model=Route
		attrs = {'class':'table table-striped'}
		fields = ('wall', 'color', 'grade','name', 'setter', 'date_set', 'comment')


