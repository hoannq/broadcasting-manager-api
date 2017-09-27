from django.core.management.base import BaseCommand, CommandError

#### Step 5
from seeders.broadcastings import BroadcastingSeeder

class Command(BaseCommand):
    help = 'Import broadcasting data'

    def handle(self, *args, **options):
        #### Step 5
        BroadcastingSeeder()
        self.stdout.write(self.style.SUCCESS('Import broadcasting data successfully'))