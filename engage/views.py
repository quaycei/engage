from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.contrib import messages

def tools(request):
    return redirect('tool_list') 