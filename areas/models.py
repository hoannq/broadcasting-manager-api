from django.db import models

# Create your models here.
AREAS = (
    (1, 'Tây Bắc'),
    (2, 'Đông Bắc'),
    (3, 'Đồng Bằng Sông Hồng'),
    (4, 'Bấc Trung Bộ'),
    (5, 'Nam Trung Bộ'),
    (6, 'Tây Nguyên'),
    (7, 'Đông Nam Bộ'),
    (8, 'Đồng Bằng Sông Cửu Long'),
)

class Area(models.Model):
    name = models.CharField(choices=AREAS)
