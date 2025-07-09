from django.apps import AppConfig


class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals  # Регистрируем сигнал
