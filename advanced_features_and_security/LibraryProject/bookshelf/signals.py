from django.apps import apps
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.label == "bookshelf":  # only run for this app
        Book = apps.get_model('bookshelf', 'Book')

        # Create groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Get permissions
        can_view = Permission.objects.get(codename="can_view")
        can_create = Permission.objects.get(codename="can_create")
        can_edit = Permission.objects.get(codename="can_edit")
        can_delete = Permission.objects.get(codename="can_delete")

        # Assign permissions
        editors.permissions.set([can_view, can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])
