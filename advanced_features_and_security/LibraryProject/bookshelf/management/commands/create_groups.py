from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book


class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Ensure permissions exist
        permissions = Permission.objects.filter(content_type__app_label="bookshelf", content_type__model="book")

        # Create Editors group
        editors, created = Group.objects.get_or_create(name="Editors")
        if created:
            editors.permissions.set(permissions)  # all perms
            self.stdout.write(self.style.SUCCESS("Editors group created with all permissions."))

        # Create Viewers group
        viewers, created = Group.objects.get_or_create(name="Viewers")
        if created:
            view_perm = permissions.get(codename="can_view")
            viewers.permissions.add(view_perm)
            self.stdout.write(self.style.SUCCESS("Viewers group created with view permission."))

