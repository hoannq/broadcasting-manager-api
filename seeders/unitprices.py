from machinelocations.models import Machinelocation
from unitprices.models import Unitprice

UNITPRICES = [
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk=1),
        'price':  89000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  73000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  59000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  83000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  68000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  53000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  93000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  77000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  62000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  85000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  69000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 1),
        'price':  55000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  91000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  75000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  61000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  84000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  69000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  54000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  96000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  80000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  65000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  86000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  71000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 2),
        'price':  56000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  94000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  79000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  64000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  86000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  71000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  56000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  100000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  84000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  70000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  88000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  73000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 3),
        'price':  58000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  95000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  78000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  62000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  89000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  72000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  56000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  98000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  80000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  64000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  90000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  73000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 4),
        'price':  57000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  97000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  80000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  64000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  90000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  73000
    },
    {
        'broadcasting_hours':  "19",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  57000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  101000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  83000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  1, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  67000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "10",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  91000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "5",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  75000
    },
    {
        'broadcasting_hours':  "24",
        'renew':  0, # 1 = thứ nhất, 0 = thứ hai
        'power_type':  "2",
        'machine_location': Machinelocation.objects.get(pk = 5),
        'price':  59000
    },
]

class UnitpriceSeeder():
    def __init__(self):
        Unitprice.objects.all().delete()
        for unitPrice in UNITPRICES:
            new_price = Unitprice(broadcasting_hours=unitPrice['broadcasting_hours'],
                                  renew=unitPrice['renew'],
                                  power_type=unitPrice['power_type'],
                                  price=unitPrice['price'],
                                  machine_location=unitPrice['machine_location'])
            new_price.save()