from django import template

register = template.Library()

@register.filter(name='article_shorten_body')
def article_shorten_body(bodytext, length):
	if len(bodytext) > length:
		text = "%s ... " % bodytext[1:length]
	else:
		text = bodytext

	return text