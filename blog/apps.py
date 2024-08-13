# from django.apps import AppConfig

# class BlogConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'blog'

#     def ready(self):
#         import blog.signals  # Import the signals to connect them
from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = "Blog Application"

    def ready(self):
        import blog.signals
