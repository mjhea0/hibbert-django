from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Article

class ArticleResource(ModelResource):
	class Meta:
		queryset = Article.objects.all()
		resource_name = 'article'
		filtering = { "title" : ALL }