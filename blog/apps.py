from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = "Blog Application"

    def ready(self):
        import blog.signals
