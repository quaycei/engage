from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



ENTITY_TYPES = (
        (0, 'Individual'),
        (1, 'Team'),
        (2, 'Organization'),
    )


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entity = models.IntegerField(choices=ENTITY_TYPES, default=0)
    is_ibmer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_collaborator(sender, instance, created, **kwargs):
    if created:
        Collaborator.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_collaborator(sender, instance, **kwargs):
    instance.collaborator.save()




class Relationship(models.Model):
	parent = models.ForeignKey(Collaborator, default=None, blank=True, null=True)
	children = models.ManyToManyField('Collaborator', related_name='children', default=None, blank=True)
