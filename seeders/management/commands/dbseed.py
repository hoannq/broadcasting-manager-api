from django.core.management.base import BaseCommand, CommandError
from seeders.areas import AreaSeeder
from seeders.televisions import TelevisionSeeder
from seeders.machinelocations import MachinelocationSeeder

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        AreaSeeder()
        TelevisionSeeder()
        MachinelocationSeeder()
        self.stdout.write(self.style.SUCCESS('Successfully'))