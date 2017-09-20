from machinelocations.models import Machinelocation

LOCARIONS = [
    {
        'name': 'Địa điểm đặt máy cùng với Đài địa phương',
        'owner': 'Đài Truyền hình Quốc gia'
    },
    {
        'name': 'Địa điểm đặt máy đặc biệt khó khăn',
        'owner': 'Đài Truyền hình Quốc gia'
    },
    {
        'name': 'Cụm máy phát độc lập của Đài Truyền hình Quốc gia',
        'owner': 'Đài Truyền hình Quốc gia'
    },
    {
        'name': 'Địa điểm đặt máy bình thường',
        'owner': 'Đài Truyền hình Địa phương'
    },
    {
        'name': 'Địa điểm đặt máy đặc biệt khó khăn',
        'owner': 'Đài Truyền hình Địa phương'
    },
]

class MachinelocationSeeder():
    def __init__(self):
        Machinelocation.objects.all().delete()
        for location in LOCARIONS:
            new_location = Machinelocation(name=location['name'], owner=location['owner'])
            new_location.save()