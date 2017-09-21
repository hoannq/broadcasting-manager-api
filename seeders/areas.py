from areas.models import Area

AREAS = [
    {'name': 'Tây Bắc'},
    {'name': 'Đông Bắc'},
    {'name': 'Đồng Bằng Sông Hồng'},
    {'name': 'Bắc Trung Bộ'},
    {'name': 'Nam Trung Bộ'},
    {'name': 'Tây Nguyên'},
    {'name': 'Đông Nam Bộ'},
    {'name': 'Đồng Bằng Sông Cửu Long'},
]

class AreaSeeder():
    def __init__(self):
        Area.objects.all().delete()
        for area in AREAS:
            new_area = Area(name=area['name'])
            new_area.save()