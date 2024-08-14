# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Post, Notification

# @receiver(post_save, sender=Post)
# def create_notification(sender, instance, created, **kwargs):
#     if created:
#         message = f'You have created a new post: {instance.title}'
#     else:
#         message = f'You have updated your post: {instance.title}'

#     Notification.objects.create(user=instance.author, message=message)

#     Notification.objects.create(user=instance.author, message=message)

