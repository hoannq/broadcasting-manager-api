from django.core.management.base import BaseCommand, CommandError

#### Step 3
from seeders.broadcasts import BroadcastSeeder

class Command(BaseCommand):
    help = 'Import broadcasting programmer data'

    def handle(self, *args, **options):
        #### Step 3
        BroadcastSeeder()
        self.stdout.write(self.style.SUCCESS('Import broadcasting programmer data successfully'))