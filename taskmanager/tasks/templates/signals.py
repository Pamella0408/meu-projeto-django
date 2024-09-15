from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from datetime import timedelta
from django.utils import timezone

@receiver(post_save, sender=Task)
def task_deadline_notification(sender, instance, **kwargs):
    if instance.deadline - timezone.now() <= timedelta(days=1):
        # Exiba uma mensagem ou envie um email de notificação
        print(f"Tarefa {instance.title} está próxima do vencimento!")

