from django.db import models

# Create your models here.
TELEVISIONS = [ 'Đài Truyền hình Quốc gia', 'Đài Truyền hình Địa phương', ]

LOCATIONS = [
    'Địa điểm đặt máy cùng với Đài địa phương',
    'Địa điểm đặt máy đặc biệt khó khăn',
    'Cụm máy phát độc lập của Đài Truyền hình Quốc gia',
    'Địa điểm đặt máy bình thường',
    'Địa điểm đặt máy đặc biệt khó khăn',
]

class Machinelocation(models.Model):
    name = models.CharField(choices=LOCATIONS)
    owner = models.CharField(choices=TELEVISIONS)