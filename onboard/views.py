from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse


def dashboard(request):
	return render(request, 'onboard/dashboard.html')