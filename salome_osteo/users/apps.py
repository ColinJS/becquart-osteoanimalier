from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "salome_osteo.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import salome_osteo.users.signals  # noqa F401
        except ImportError:
            pass
