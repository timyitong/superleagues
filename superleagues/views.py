from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse


def home(request,template_name='superleagues/index.html'):
	data = {}
	return render(request, template_name, data)
