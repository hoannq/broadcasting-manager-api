import datetime

from broadcasts.models import Broadcast
from contracts.models import Contract
from broadcastingstatus.models import Broadcastingstatus
from timeranges.models import Timerange

class BroadcastingSeeder():
    def __init__(self):
        year = 2015
        now = datetime.datetime.now()
        start_day = datetime.date(year, 1, 1)
        broadcasts = Broadcast.objects.all()

        while(start_day < now.date()):
            for broadcast in broadcasts:
                segments = broadcast.time_segment

                contract_start_date = broadcast.contract_start_date
                contract_end_date = broadcast.contract_end_date

                contract = Contract.objects.exclude(cancel_date=None).filter(broadcast=broadcast.pk).first()

                check = (start_day >= contract_start_date) and (start_day <= (contract_end_date + datetime.timedelta(days=1)))

                if contract is not None:
                    check = (start_day >= contract_start_date) and (start_day <= (contract_end_date + datetime.timedelta(days=1))) and (start_day <= contract.cancel_date + datetime.timedelta(days=1))

                if check:
                    if segments == 1:
                        broadcasting_status = Broadcastingstatus(
                            date=start_day,
                            power_T='500',
                            power_PX='5000',
                            reporter='Nguyen Van A',
                            status='Binh thuong',
                            broadcast=broadcast
                        )
                        broadcasting_status.save()

                        Timerange(
                            type=1,
                            start_time=datetime.time.min,
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()
                        print(broadcasting_status)

                    if segments == 2:
                        broadcasting_status = Broadcastingstatus(
                            date=start_day,
                            power_T='500',
                            power_PX='5000',
                            reporter='Nguyen Van A',
                            status='Binh thuong',
                            broadcast=broadcast
                        )
                        broadcasting_status.save()

                        Timerange(
                            type=1,
                            start_time=datetime.time.min,
                            end_time=datetime.time(17, 0, 0),
                            broadcasting_status=broadcasting_status
                        ).save()

                        Timerange(
                            type=1,
                            start_time=datetime.time(20, 0, 0),
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()
                        print(broadcasting_status)

                    if segments == 3:
                        broadcasting_status = Broadcastingstatus(
                            date=start_day,
                            power_T='500',
                            power_PX='5000',
                            reporter='Nguyen Van A',
                            status='Binh thuong',
                            broadcast=broadcast
                        )
                        broadcasting_status.save()

                        Timerange(
                            type=1,
                            start_time=datetime.time.min,
                            end_time=datetime.time(11, 0, 0),
                            broadcasting_status=broadcasting_status
                        ).save()

                        Timerange(
                            type=1,
                            start_time=datetime.time(11, 40, 00),
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()

                        Timerange(
                            type=1,
                            start_time=datetime.time(21, 30, 00),
                            end_time=datetime.time.max,
                            broadcasting_status=broadcasting_status
                        ).save()
                        print(broadcasting_status)

            start_day += datetime.timedelta(days=1)