from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from tools.models import Tag, Tool

def tool_list(request):
	tools = Tool.objects.all()
	tags = Tag.objects.all()


	return render(request, 'tools/list.html', {
		'tools':tools,
		'tags':tags,
		})