from django.core.management.base import BaseCommand, CommandError

#### Step 4
from seeders.contracts import ContractSeeder

class Command(BaseCommand):
    help = 'Import contract data'

    def handle(self, *args, **options):
        #### Step 4
        ContractSeeder()
        self.stdout.write(self.style.SUCCESS('Import contract data successfully'))