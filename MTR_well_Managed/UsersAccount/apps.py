from django.apps import AppConfig


class UsersaccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UsersAccount'

    def ready(self):
        import UsersAccount.signals