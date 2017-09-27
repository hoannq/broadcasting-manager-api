from basestations.models import Basestation
from broadcasts.models import Broadcast

BROADCASTS = [
    ## id: 1
    ## Trạm: Phòng phát sóng Vệ tinh Giảng Võ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "",
        'power': "0.25",
        'broadcasting_type': "Vệ Tinh",
        'time_segment': 1,
        'machine_brand': "",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=1)
    },
    ## id: 2
    ## Trạm: Phòng phát sóng Hà Nội
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "9",
        'power': "30",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Plish",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=2)
    },
    ## id: 3
    ## Trạm: Phòng phát sóng Hà Nội
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "11",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=2)
    },
    ## id: 4
    ## Trạm: Phòng phát sóng Hà Nội
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "22",
        'power': "20",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "THOMCAST",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=2)
    },
    ## id: 5
    ## Trạm: Phòng phát sóng Hà Nội
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "54",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=2)
    },
    ## id: 6
    ## Trạm: Phòng phát sóng Hà Nội
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "51",
        'power': "5",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=2)
    },
    ## id: 7
    ## Trạm: Phòng phát sóng Tam Đảo
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "3",
        'power': "20",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "THOMCAST",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=3)
    },
    ## id: 8
    ## Trạm: Phòng phát sóng Tam Đảo
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "26",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=3)
    },
    ## id: 9
    ## Trạm: Phòng phát sóng THQG Hải Phòng
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "43",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=4)
    },
    ## id: 10
    ## Trạm: Phòng Quản lý phát sóng Bắc Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "22",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=5)
    },
    ## id: 11
    ## Trạm: Phòng Quản lý phát sóng Bắc Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "46",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=5)
    },
    ## id: 12
    ## Trạm: Phòng Quản lý phát sóng Bắc Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "7",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "THOMCAST",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=5)
    },
    ## id: 13
    ## Trạm: Phòng Quản lý phát sóng Bắc Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "41",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=5)
    },
    ## id: 14
    ## Trạm: Phòng Quản lý phát sóng Bắc Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_Hue",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=5)
    },
    ## id: 15
    ## Trạm: Phòng Quản lý phát sóng Miền Trung
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=6)
    },
    ## id: 16
    ## Trạm: Phòng Quản lý phát sóng Miền Trung
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "26",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=6)
    },
    ## id: 17
    ## Trạm: Phòng Quản lý phát sóng Miền Trung
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=6)
    },
    ## id: 18
    ## Trạm: Phòng Quản lý phát sóng Miền Trung
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "47",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=6)
    },
    ## id: 19
    ## Trạm: Phòng Quản lý phát sóng Miền Trung
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "49",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6;VTV_DaNang",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=6)
    },
    ## id: 20
    ## Trạm: Phòng Quản lý phát sóng Miền Trung
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_DaNang",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "9",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=6)
    },
    ## id: 21
    ## Trạm: Phòng Quản lý phát sóng Nam Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "9",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=7)
    },
    ## id: 22
    ## Trạm: Phòng Quản lý phát sóng Nam Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=7)
    },
    ## id: 23
    ## Trạm: Phòng Quản lý phát sóng Nam Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=7)
    },
    ## id: 24
    ## Trạm: Phòng Quản lý phát sóng Nam Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "41",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=7)
    },
    ## id: 25
    ## Trạm: Phòng Quản lý phát sóng Nam Trung Bộ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_PhuYen",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "7",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=7)
    },
    ## id: 26
    ## Trạm: Phòng phát sóng Bình Dương
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "50",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Toshiba",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=8)
    },
    ## id: 27
    ## Trạm: Phòng phát sóng Bình Dương
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "46",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=8)
    },
    ## id: 28
    ## Trạm: Phòng phát sóng Bình Dương
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "28",
        'power': "50",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Toshiba",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=8)
    },
    ## id: 29
    ## Trạm: Phòng phát sóng Bình Dương
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "48",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=8)
    },
    ## id: 30
    ## Trạm: Phòng phát sóng Bình Dương
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "5",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6;VTV_DaNang",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=8)
    },
    ## id: 31
    ## Trạm: Phòng phát sóng THQG Bà Rịa - Vũng Tàu
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "38",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=9)
    },
    ## id: 32
    ## Trạm: Phòng phát sóng THQG Bà Rịa - Vũng Tàu
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "61",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=9)
    },
    ## id: 33
    ## Trạm: Phòng phát sóng THQG Bà Rịa - Vũng Tàu
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "24",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=9)
    },
    ## id: 34
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "46",
        'power': "30",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VIHITECH",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 35
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 36
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "20",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 37
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "22",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 38
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "45",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 39
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTVCT1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "49",
        'power': "30",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 40
    ## Trạm: Phòng phát sóng Cần Thơ
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTVCT2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "51",
        'power': "30",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=10)
    },
    ## id: 41
    ## Trạm: Phòng phát sóng Cần Thơ tại Núi Sam
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTVCT1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "56",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "HARIS",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=11)
    },
    ## id: 42
    ## Trạm: Phòng phát sóng Cần Thơ tại Núi Sam
    ## Đài: TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam
    {
        'name': "VTVCT2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "11",
        'power': "0.1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 0, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 1, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=11)
    },
    ## id: 43
    ## Trạm: Hà Giang
    ## Đài: ĐÀI PTTH HÀ GIANG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "8",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=12)
    },
    ## id: 44
    ## Trạm: Hà Giang
    ## Đài: ĐÀI PTTH HÀ GIANG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=12)
    },
    ## id: 45
    ## Trạm: Hà Giang
    ## Đài: ĐÀI PTTH HÀ GIANG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 2,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=12)
    },
    ## id: 46
    ## Trạm: Lào Cai
    ## Đài: ĐÀI PTTH TỈNH LÀO CAI
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=13)
    },
    ## id: 47
    ## Trạm: Lào Cai
    ## Đài: ĐÀI PTTH TỈNH LÀO CAI
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=13)
    },
    ## id: 48
    ## Trạm: Lào Cai
    ## Đài: ĐÀI PTTH TỈNH LÀO CAI
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=13)
    },
    ## id: 49
    ## Trạm: Lào Cai
    ## Đài: ĐÀI PTTH TỈNH LÀO CAI
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=13)
    },
    ## id: 50
    ## Trạm: Cao Bằng
    ## Đài: ĐÀI PTTH TỈNH CAO BẰNG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "0.5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "thcst",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=14)
    },
    ## id: 51
    ## Trạm: Cao Bằng
    ## Đài: ĐÀI PTTH TỈNH CAO BẰNG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "11",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 3,
        'machine_brand': "thson",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=14)
    },
    ## id: 52
    ## Trạm: Cao Bằng
    ## Đài: ĐÀI PTTH TỈNH CAO BẰNG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=14)
    },
    ## id: 53
    ## Trạm: Điện Biên
    ## Đài: ĐÀI PTTH ĐIỆN BIÊN
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=15)
    },
    ## id: 54
    ## Trạm: Điện Biên
    ## Đài: ĐÀI PTTH ĐIỆN BIÊN
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=15)
    },
    ## id: 55
    ## Trạm: Điện Biên
    ## Đài: ĐÀI PTTH ĐIỆN BIÊN
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=15)
    },
    ## id: 56
    ## Trạm: Điện Biên
    ## Đài: ĐÀI PTTH ĐIỆN BIÊN
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=15)
    },
    ## id: 57
    ## Trạm: Lai Châu
    ## Đài: ĐÀI PTTH LAI CHÂU
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=16)
    },
    ## id: 58
    ## Trạm: Lai Châu
    ## Đài: ĐÀI PTTH LAI CHÂU
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=16)
    },
    ## id: 59
    ## Trạm: Lai Châu
    ## Đài: ĐÀI PTTH LAI CHÂU
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=16)
    },
    ## id: 60
    ## Trạm: Tuyên Quang
    ## Đài: ĐÀI PTTH TUYÊN QUANG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "34",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=17)
    },
    ## id: 61
    ## Trạm: Tuyên Quang
    ## Đài: ĐÀI PTTH TUYÊN QUANG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "26",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=17)
    },
    ## id: 62
    ## Trạm: Yên Bái
    ## Đài: ĐÀI PTTH YÊN BÁI
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=18)
    },
    ## id: 63
    ## Trạm: Yên Bái
    ## Đài: ĐÀI PTTH YÊN BÁI
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=18)
    },
    ## id: 64
    ## Trạm: Yên Bái
    ## Đài: ĐÀI PTTH YÊN BÁI
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "27",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=18)
    },
    ## id: 65
    ## Trạm: Sơn La
    ## Đài: ĐÀI PTTH SƠN LA
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=19)
    },
    ## id: 66
    ## Trạm: Sơn La
    ## Đài: ĐÀI PTTH SƠN LA
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=19)
    },
    ## id: 67
    ## Trạm: Sơn La
    ## Đài: ĐÀI PTTH SƠN LA
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=19)
    },
    ## id: 68
    ## Trạm: Bắc Kạn
    ## Đài: ĐÀI PTTH BẮC KẠN
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "1.5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Intedico",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=20)
    },
    ## id: 69
    ## Trạm: Bắc Kạn
    ## Đài: ĐÀI PTTH BẮC KẠN
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=20)
    },
    ## id: 70
    ## Trạm: Bắc Kạn
    ## Đài: ĐÀI PTTH BẮC KẠN
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=20)
    },
    ## id: 71
    ## Trạm: Bắc Kạn
    ## Đài: ĐÀI PTTH BẮC KẠN
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "33",
        'power': "0.5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Italia",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=20)
    },
    ## id: 72
    ## Trạm: Lạng Sơn
    ## Đài: ĐÀI PTTH LẠNG SƠN
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=21)
    },
    ## id: 73
    ## Trạm: Lạng Sơn
    ## Đài: ĐÀI PTTH LẠNG SƠN
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=21)
    },
    ## id: 74
    ## Trạm: Lạng Sơn
    ## Đài: ĐÀI PTTH LẠNG SƠN
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "7",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=21)
    },
    ## id: 75
    ## Trạm: Lạng Sơn - Mẫu Sơn
    ## Đài: ĐÀI PTTH LẠNG SƠN
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "33",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Italia",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=22)
    },
    ## id: 76
    ## Trạm: Hòa Bình
    ## Đài: ĐÀI PTTH HÒA BÌNH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=23)
    },
    ## id: 77
    ## Trạm: Hòa Bình
    ## Đài: ĐÀI PTTH HÒA BÌNH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "28",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=23)
    },
    ## id: 78
    ## Trạm: Hòa Bình
    ## Đài: ĐÀI PTTH HÒA BÌNH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "33",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=23)
    },
    ## id: 79
    ## Trạm: Hòa Bình
    ## Đài: ĐÀI PTTH HÒA BÌNH
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "0.5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=23)
    },
    ## id: 80
    ## Trạm: Hải Phòng
    ## Đài: ĐÀI PTTH THÀNH PHỐ HẢI PHÒNG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "thcst",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=24)
    },
    ## id: 81
    ## Trạm: Quảng Ninh Hạ Long
    ## Đài: ĐÀI PTTH QUẢNG NINH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "33",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=25)
    },
    ## id: 82
    ## Trạm: Quảng Ninh Hạ Long
    ## Đài: ĐÀI PTTH QUẢNG NINH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=25)
    },
    ## id: 83
    ## Trạm: Quảng Ninh Hạ Long
    ## Đài: ĐÀI PTTH QUẢNG NINH
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "31",
        'power': "10",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=25)
    },
    ## id: 84
    ## Trạm: Quảng Ninh Móng Cái
    ## Đài: ĐÀI PTTH QUẢNG NINH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=26)
    },
    ## id: 85
    ## Trạm: Quảng Ninh Móng Cái
    ## Đài: ĐÀI PTTH QUẢNG NINH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=26)
    },
    ## id: 86
    ## Trạm: Quảng Ninh Móng Cái
    ## Đài: ĐÀI PTTH QUẢNG NINH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=26)
    },
    ## id: 87
    ## Trạm: Thái Bình
    ## Đài: ĐÀI PTTH THÁI BÌNH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "32",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=27)
    },
    ## id: 88
    ## Trạm: Thái Bình
    ## Đài: ĐÀI PTTH THÁI BÌNH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Thosn",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=27)
    },
    ## id: 89
    ## Trạm: Nam Định
    ## Đài: ĐÀI PTTH NAM ĐỊNH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=28)
    },
    ## id: 90
    ## Trạm: Nam Định
    ## Đài: ĐÀI PTTH NAM ĐỊNH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "50",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=28)
    },
    ## id: 91
    ## Trạm: Nam Định
    ## Đài: ĐÀI PTTH NAM ĐỊNH
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "53",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=28)
    },
    ## id: 92
    ## Trạm: Ninh Bình
    ## Đài: ĐÀI PTTH NINH BÌNH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=29)
    },
    ## id: 93
    ## Trạm: Ninh Bình
    ## Đài: ĐÀI PTTH NINH BÌNH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=29)
    },
    ## id: 94
    ## Trạm: Thanh Hóa - Quyết Thắng
    ## Đài: ĐÀI PTTH THANH HOÁ
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "24",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=30)
    },
    ## id: 95
    ## Trạm: Thanh Hóa - Quyết Thắng
    ## Đài: ĐÀI PTTH THANH HOÁ
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "CTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=30)
    },
    ## id: 96
    ## Trạm: Thanh Hóa - Quyết Thắng
    ## Đài: ĐÀI PTTH THANH HOÁ
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "7",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Optm",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=30)
    },
    ## id: 97
    ## Trạm: Thanh Hóa - Quyết Thắng
    ## Đài: ĐÀI PTTH THANH HOÁ
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "40",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=30)
    },
    ## id: 98
    ## Trạm: Thanh Hóa - Bá Thước
    ## Đài: ĐÀI PTTH THANH HOÁ
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Italia",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=31)
    },
    ## id: 99
    ## Trạm: Nghệ An
    ## Đài: ĐÀI PTTH NGHỆ AN
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=32)
    },
    ## id: 100
    ## Trạm: Nghệ An
    ## Đài: ĐÀI PTTH NGHỆ AN
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=32)
    },
    ## id: 101
    ## Trạm: Nghệ An
    ## Đài: ĐÀI PTTH NGHỆ AN
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "43",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=32)
    },
    ## id: 102
    ## Trạm: Hà Tĩnh - Thiên Tượng
    ## Đài: ĐÀI PTTH HÀ TĨNH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Alpha",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=33)
    },
    ## id: 103
    ## Trạm: Hà Tĩnh - Thiên Tượng
    ## Đài: ĐÀI PTTH HÀ TĨNH
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "9",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Thomson",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=33)
    },
    ## id: 104
    ## Trạm: Hà Tĩnh
    ## Đài: ĐÀI PTTH HÀ TĨNH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=34)
    },
    ## id: 105
    ## Trạm: Hà Tĩnh
    ## Đài: ĐÀI PTTH HÀ TĨNH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "26",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=34)
    },
    ## id: 106
    ## Trạm: Hà Tĩnh
    ## Đài: ĐÀI PTTH HÀ TĨNH
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=34)
    },
    ## id: 107
    ## Trạm: Quảng Bình
    ## Đài: ĐÀI PTTH QUẢNG BÌNH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=35)
    },
    ## id: 108
    ## Trạm: Quảng Bình
    ## Đài: ĐÀI PTTH QUẢNG BÌNH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "CTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=35)
    },
    ## id: 109
    ## Trạm: Quảng Bình
    ## Đài: ĐÀI PTTH QUẢNG BÌNH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=35)
    },
    ## id: 110
    ## Trạm: Quảng Trị
    ## Đài: ĐÀI PTTH QUẢNG TRỊ
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=36)
    },
    ## id: 111
    ## Trạm: Quảng Trị
    ## Đài: ĐÀI PTTH QUẢNG TRỊ
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Thomson",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=36)
    },
    ## id: 112
    ## Trạm: Quảng Trị
    ## Đài: ĐÀI PTTH QUẢNG TRỊ
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "30",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=36)
    },
    ## id: 113
    ## Trạm: Quảng Nam
    ## Đài: ĐÀI PTTH QUẢNG NAM
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=37)
    },
    ## id: 114
    ## Trạm: Quảng Nam
    ## Đài: ĐÀI PTTH QUẢNG NAM
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "VTC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=37)
    },
    ## id: 115
    ## Trạm: Quảng Nam
    ## Đài: ĐÀI PTTH QUẢNG NAM
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "33",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=37)
    },
    ## id: 116
    ## Trạm: Quảng Ngãi
    ## Đài: ĐÀI PTTH QUẢNG NGÃI
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Thocst",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=38)
    },
    ## id: 117
    ## Trạm: Quảng Ngãi
    ## Đài: ĐÀI PTTH QUẢNG NGÃI
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "thson",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=38)
    },
    ## id: 118
    ## Trạm: Quảng Ngãi
    ## Đài: ĐÀI PTTH QUẢNG NGÃI
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "35",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=38)
    },
    ## id: 119
    ## Trạm: Bình Định
    ## Đài: ĐÀI PTTH BÌNH ĐỊNH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=39)
    },
    ## id: 120
    ## Trạm: Bình Định
    ## Đài: ĐÀI PTTH BÌNH ĐỊNH
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "TQT",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=39)
    },
    ## id: 121
    ## Trạm: Bình Định
    ## Đài: ĐÀI PTTH BÌNH ĐỊNH
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=39)
    },
    ## id: 122
    ## Trạm: Bình Định
    ## Đài: ĐÀI PTTH BÌNH ĐỊNH
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "10",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "TQT",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=39)
    },
    ## id: 123
    ## Trạm: Khánh Hòa
    ## Đài: ĐÀI PTTH KHÁNH HOÀ
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=40)
    },
    ## id: 124
    ## Trạm: Khánh Hòa
    ## Đài: ĐÀI PTTH KHÁNH HOÀ
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "22",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=40)
    },
    ## id: 125
    ## Trạm: Khánh Hòa
    ## Đài: ĐÀI PTTH KHÁNH HOÀ
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "TQT",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=40)
    },
    ## id: 126
    ## Trạm: Khánh Hòa
    ## Đài: ĐÀI PTTH KHÁNH HOÀ
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "31",
        'power': "10",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=40)
    },
    ## id: 127
    ## Trạm: Ninh Thuận
    ## Đài: ĐÀI PTTH NINH THUẬN
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=41)
    },
    ## id: 128
    ## Trạm: Ninh Thuận
    ## Đài: ĐÀI PTTH NINH THUẬN
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "30",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=41)
    },
    ## id: 129
    ## Trạm: Ninh Thuận
    ## Đài: ĐÀI PTTH NINH THUẬN
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=41)
    },
    ## id: 130
    ## Trạm: Bình Thuận
    ## Đài: ĐÀI PTTH BÌNH THUẬN
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=42)
    },
    ## id: 131
    ## Trạm: Bình Thuận
    ## Đài: ĐÀI PTTH BÌNH THUẬN
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "26",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=42)
    },
    ## id: 132
    ## Trạm: Bình Thuận
    ## Đài: ĐÀI PTTH BÌNH THUẬN
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "28",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=42)
    },
    ## id: 133
    ## Trạm: Kon Tum
    ## Đài: ĐÀI PTTH KON TUM
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=43)
    },
    ## id: 134
    ## Trạm: Kon Tum
    ## Đài: ĐÀI PTTH KON TUM
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=43)
    },
    ## id: 135
    ## Trạm: Kon Tum
    ## Đài: ĐÀI PTTH KON TUM
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=43)
    },
    ## id: 136
    ## Trạm: Gia Lai Hàm Rồng
    ## Đài: ĐÀI PTTH GIA LAI
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "9",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=44)
    },
    ## id: 137
    ## Trạm: Gia Lai Hàm Rồng
    ## Đài: ĐÀI PTTH GIA LAI
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "7",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "TQT",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=44)
    },
    ## id: 138
    ## Trạm: Gia Lai Hàm Rồng
    ## Đài: ĐÀI PTTH GIA LAI
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=44)
    },
    ## id: 139
    ## Trạm: Đắk Lắk Hà Lan
    ## Đài: ĐÀI PTTH ĐẮK LẮK
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=45)
    },
    ## id: 140
    ## Trạm: Đắk Lắk Hà Lan
    ## Đài: ĐÀI PTTH ĐẮK LẮK
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "31",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=45)
    },
    ## id: 141
    ## Trạm: Đắk Lắk Hà Lan
    ## Đài: ĐÀI PTTH ĐẮK LẮK
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "28",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=45)
    },
    ## id: 142
    ## Trạm: Đắk Lắk BMT
    ## Đài: ĐÀI PTTH ĐẮK LẮK
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "19",
        'frequency_channel': "8",
        'power': "0.3",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "TQT",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=46)
    },
    ## id: 143
    ## Trạm: Đắk Lắk BMT
    ## Đài: ĐÀI PTTH ĐẮK LẮK
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "38",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "TQT",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=46)
    },
    ## id: 144
    ## Trạm: Đắk Nông
    ## Đài: ĐÀI PTTH ĐẮK NÔNG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=47)
    },
    ## id: 145
    ## Trạm: Đắk Nông
    ## Đài: ĐÀI PTTH ĐẮK NÔNG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "24",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=47)
    },
    ## id: 146
    ## Trạm: Đắk Nông
    ## Đài: ĐÀI PTTH ĐẮK NÔNG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=47)
    },
    ## id: 147
    ## Trạm: Đắk Nông
    ## Đài: ĐÀI PTTH ĐẮK NÔNG
    {
        'name': "VTV6",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "6",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Thomson",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=47)
    },
    ## id: 148
    ## Trạm: Lâm Đồng Đà Lạt
    ## Đài: ĐÀI PTTH LÂM ĐỒNG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "1",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "thcst",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=48)
    },
    ## id: 149
    ## Trạm: Lâm Đồng Cầu Đất
    ## Đài: ĐÀI PTTH LÂM ĐỒNG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "9",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=49)
    },
    ## id: 150
    ## Trạm: Lâm Đồng Cầu Đất
    ## Đài: ĐÀI PTTH LÂM ĐỒNG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "25",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=49)
    },
    ## id: 151
    ## Trạm: Lâm Đồng Cầu Đất
    ## Đài: ĐÀI PTTH LÂM ĐỒNG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "11",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Thalse",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=49)
    },
    ## id: 152
    ## Trạm: Bình Phước
    ## Đài: ĐÀI PTTH BÌNH PHƯỚC
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "8",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "thcst",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=50)
    },
    ## id: 153
    ## Trạm: Bình Phước
    ## Đài: ĐÀI PTTH BÌNH PHƯỚC
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=50)
    },
    ## id: 154
    ## Trạm: Bình Phước
    ## Đài: ĐÀI PTTH BÌNH PHƯỚC
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "12",
        'power': "0.5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Inteco",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=50)
    },
    ## id: 155
    ## Trạm: Tây Ninh
    ## Đài: ĐÀI PTTH TÂY NINH
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "22",
        'power': "2",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "thcst",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=51)
    },
    ## id: 156
    ## Trạm: An Giang
    ## Đài: ĐÀI PTTH AN GIANG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "24",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=52)
    },
    ## id: 157
    ## Trạm: An Giang
    ## Đài: ĐÀI PTTH AN GIANG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "53",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=52)
    },
    ## id: 158
    ## Trạm: An Giang
    ## Đài: ĐÀI PTTH AN GIANG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "41",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=52)
    },
    ## id: 159
    ## Trạm: An Giang
    ## Đài: ĐÀI PTTH AN GIANG
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=52)
    },
    ## id: 160
    ## Trạm: Bến Tre
    ## Đài: ĐÀI PTTH BẾN TRE
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "37",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=53)
    },
    ## id: 161
    ## Trạm: Bến Tre
    ## Đài: ĐÀI PTTH BẾN TRE
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "40",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=53)
    },
    ## id: 162
    ## Trạm: Bến Tre
    ## Đài: ĐÀI PTTH BẾN TRE
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "52",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=53)
    },
    ## id: 163
    ## Trạm: Bến Tre
    ## Đài: ĐÀI PTTH BẾN TRE
    {
        'name': "VTV_So",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "2",
        'broadcasting_type': "Số",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "VTV1;VTV2;VTV3;VTV6",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=53)
    },
    ## id: 164
    ## Trạm: Sóc Trăng
    ## Đài: ĐÀI PTTH SÓC TRĂNG
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "50",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 2,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=54)
    },
    ## id: 165
    ## Trạm: Kiên Giang Hà Tiên
    ## Đài: ĐÀI PTTH KIÊN GIANG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "47",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=55)
    },
    ## id: 166
    ## Trạm: Kiên Giang Hòn Me
    ## Đài: ĐÀI PTTH KIÊN GIANG
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "23",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=56)
    },
    ## id: 167
    ## Trạm: Kiên Giang Hòn Me
    ## Đài: ĐÀI PTTH KIÊN GIANG
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "28",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "NEC",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=56)
    },
    ## id: 168
    ## Trạm: Bạc Liêu
    ## Đài: ĐÀI PTTH BẠC LIÊU
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "27",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=57)
    },
    ## id: 169
    ## Trạm: Bạc Liêu
    ## Đài: ĐÀI PTTH BẠC LIÊU
    {
        'name': "VTV2",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "47",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=57)
    },
    ## id: 170
    ## Trạm: Bạc Liêu
    ## Đài: ĐÀI PTTH BẠC LIÊU
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "21",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "R&S",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=57)
    },
    ## id: 171
    ## Trạm: Cà Mau
    ## Đài: ĐÀI PTTH CÀ MAU
    {
        'name': "VTV1",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "39",
        'power': "10",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Btesa",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=58)
    },
    ## id: 172
    ## Trạm: Cà Mau
    ## Đài: ĐÀI PTTH CÀ MAU
    {
        'name': "VTV3",
        'contract_start_date': "2015-01-01",
        'contract_end_date': "2018-12-31",
        'broadcasting_hours': "24",
        'frequency_channel': "42",
        'power': "5",
        'broadcasting_type': "Tương tự",
        'time_segment': 1,
        'machine_brand': "Harris",
        'description': "",
        'is_by_contract': 1, # 0 = không theo hợp đồng, 1 = theo hợp đồng
        'is_by_region': 0, # 0 = không theo khu vực, 1 = theo khu vực
        'base_station': Basestation.objects.get(pk=58)
    },
]

class BroadcastSeeder():
    def __init__(self):
        Broadcast.objects.all().delete()
        for broadcast in BROADCASTS:
            new_broadcast = Broadcast(name=broadcast['name'],
                                      contract_start_date=broadcast['contract_start_date'],
                                      contract_end_date=broadcast['contract_end_date'],
                                      broadcasting_hours=broadcast['broadcasting_hours'],
                                      frequency_channel=broadcast['frequency_channel'],
                                      power=broadcast['power'],
                                      broadcasting_type=broadcast['broadcasting_type'],
                                      time_segment=broadcast['time_segment'],
                                      machine_brand=broadcast['machine_brand'],
                                      description=broadcast['description'],
                                      is_by_contract=broadcast['is_by_contract'],
                                      is_by_region=broadcast['is_by_region'],
                                      base_station=broadcast['base_station'],
                                      )
            new_broadcast.save()