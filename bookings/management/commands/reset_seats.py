from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import ShowSeat


class Command(BaseCommand):
    help = 'Reset the status of seats to available after 5 minutes'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        self.stdout.write('seats reset to available.')
        five_minutes_ago = now - timezone.timedelta(minutes=1)
        seats = ShowSeat.objects.filter(status='selected')
        seats.update(status='available')
        self.stdout.write(f'{seats.count()} seats reset to available.')
        # , updated_at__lt=five_minutes_ago
