from django.core.management.base import BaseCommand, CommandError

#### Step 2
from seeders.unitprices import UnitpriceSeeder
from seeders.basestations import BasestaionSeeder

class Command(BaseCommand):
    help = 'Import unit price and base-station data'

    def handle(self, *args, **options):
        #### Step 2
        UnitpriceSeeder()
        BasestaionSeeder()
        self.stdout.write(self.style.SUCCESS('Import unit price and base-station data successfully'))