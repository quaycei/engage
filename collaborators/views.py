from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db import transaction

from collaborators.models import Collaborator
from collaborators.forms import UserForm, CollaboratorForm


@login_required
@transaction.atomic
def update_collaborator(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        collaborator_form = CollaboratorForm(request.POST, instance=request.user.collaborator)
        if user_form.is_valid() and collaborator_form.is_valid():
            user_form.save()
            collaborator_form.save()
            messages.success(request, ('Your collaborator was successfully updated!'))
            return redirect('update_collaborator')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        collaborator_form = CollaboratorForm(instance=request.user.collaborator)
    return render(request, 'collaborators/collaborator.html', {
        'user_form': user_form,
        'collaborator_form': collaborator_form,
    })

def collaborator_welcome(request):
	return render(request, 'collaborators/begin.html')
