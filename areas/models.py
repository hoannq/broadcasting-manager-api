from django.db import models

# Create your models here.
AREAS = (
    ('Tây Bắc', 'Tây Bắc'),
    ('Đông Bắc', 'Đông Bắc'),
    ('Đồng Bằng Sông Hồng', 'Đồng Bằng Sông Hồng'),
    ('Bắc Trung Bộ', 'Bắc Trung Bộ'),
    ('Nam Trung Bộ', 'Nam Trung Bộ'),
    ('Tây Nguyên', 'Tây Nguyên'),
    ('Đông Nam Bộ', 'Đông Nam Bộ'),
    ('Đồng Bằng Sông Cửu Long', 'Đồng Bằng Sông Cửu Long'),
)


class Area(models.Model):
    name = models.CharField(max_length=50, choices=AREAS)

    class Meta:
        db_table = "areas"