from televisions.models import Television
from areas.models import Area
from basestations.models import Basestation

BASESTATIONS = [
    {
        'name': "Phòng phát sóng Vệ tinh Giảng Võ",
        'alias_name': "Giảng Võ 1",
        'address': "43, Nguyễn Chí Thanh, phường Ngọc Khánh, quận Ba Đình, Thành phố Hà Nội",
        'location': "43, Nguyễn Chí Thanh",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,4,6SD VTV1,3,6HD BAND C",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Phòng phát sóng Hà Nội",
        'alias_name': "Giảng Võ 2 - Hà Nội",
        'address': "phường Mễ Trì, quận Nam Từ Liêm, Thành phố Hà Nội",
        'location': "Mễ Trì Hà Nội",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,6 VÀ MÁY PHÁT SỐ",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Phòng phát sóng Tam Đảo",
        'alias_name': "Tam Đảo - Vĩnh Phúc",
        'address': "Tam Đảo, Vĩnh Phúc",
        'location': "Tx Tam Đảo",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1 VÀ MÁY PHÁT SỐ",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Phòng phát sóng THQG Hải Phòng",
        'alias_name': "Trạm KTTV - Hải Phòng",
        'address': "Đồi Thiên Văn, phường Trần Thành Ngọ, quận Kiến An, Thành Phố Hải Phòng",
        'location': "Nha Khí Tượng HP",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "MÁY SỐ",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Phòng Quản lý phát sóng Bắc Trung Bộ",
        'alias_name': "Huế",
        'address': "Thừa Thiên - Huế",
        'location': "Tp Huế",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,6 VÀ KHU VỰC",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Phòng Quản lý phát sóng Miền Trung",
        'alias_name': "Đà Nẵng",
        'address': "Cao điểm 620, Đài phát sóng Quốc gia Sơn Trà, đỉnh núi Sơn Trà, bán đảo Sơn Trà, phường Thọ Quang, quận Sơn Trà, TP Đà Nẵng",
        'location': "Sơn Trà",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,6,KHU VỰC VÀ MÁY PHÁT SỐ",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Phòng Quản lý phát sóng Nam Trung Bộ",
        'alias_name': "Chóp Chài - Phú Yên",
        'address': "Phú Yên",
        'location': "Chóp Chài",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,6 VÀ KHU VỰC",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Phòng phát sóng Bình Dương",
        'alias_name': "Thủ Dầu Một - Bình Dương",
        'address': "Đài PSQG Thủ Dầu Một, Xã An Thạnh, Huyện Thuận An, Thành phố Thủ Dầu Một, tỉnh Bình Dương.",
        'location': "Thủ Dầu Một - Bình Dương",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,6 VÀ MÁY PHÁT SỐ",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=7),
    },
    {
        'name': "Phòng phát sóng THQG Bà Rịa - Vũng Tàu",
        'alias_name': "Bà Rịa - Vũng Tàu",
        'address': "Bà Rịa, Vũng Tàu",
        'location': "Tx Bà Rịa",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1, 2, 3",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=7),
    },
    {
        'name': "Phòng phát sóng Cần Thơ",
        'alias_name': "Cần Thơ",
        'address': "Đài PTTH Cần Thơ, 407 Đường 30/4, phường Hưng Lợi, quận Ninh Kiều, TP Cần Thơ",
        'location': "Tp Cần Thơ",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "VTV1,2,3,6,KHU VỰC VÀ MÁY PHÁT SỐ",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Phòng phát sóng Cần Thơ tại Núi Sam",
        'alias_name': "Cần Thơ - Núi Sam",
        'address': "Núi Sam Cần Thơ",
        'location': "Núi Sam",
        'manage_type': "Trực tiếp", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "KHU VỰC",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Hà Giang",
        'alias_name': "Hà Giang",
        'address': "Hà Giang",
        'location': "Tx Hà Giang",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=2),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Lào Cai",
        'alias_name': "Lào Cai",
        'address': "Lào Cai",
        'location': "Tp Lào Cai",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=3),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Cao Bằng",
        'alias_name': "Cao Bằng",
        'address': "Cao Bằng",
        'location': "Tx Cao Bằng",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=4),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Điện Biên",
        'alias_name': "Điện Biên",
        'address': "Điện Biên",
        'location': "Tp Điện Biên",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=5),
        'area': Area.objects.get(pk=1),
    },
    {
        'name': "Lai Châu",
        'alias_name': "Lai Châu",
        'address': "Lai Châu",
        'location': "Tx Lai Châu",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=6),
        'area': Area.objects.get(pk=1),
    },
    {
        'name': "Tuyên Quang",
        'alias_name': "Tuyên Quang",
        'address': "Tuyên Quang",
        'location': "Tx Tuyên Quang",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=7),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Yên Bái",
        'alias_name': "Yên Bái",
        'address': "Yên Bái",
        'location': "Tp Yên Bái",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=8),
        'area': Area.objects.get(pk=1),
    },
    {
        'name': "Sơn La",
        'alias_name': "Sơn La",
        'address': "Sơn La",
        'location': "Tx Sơn La",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=9),
        'area': Area.objects.get(pk=1),
    },
    {
        'name': "Bắc Kạn",
        'alias_name': "Bắc Kạn",
        'address': "Bắc Kạn",
        'location': "Tx Bắc Kạn",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=10),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Lạng Sơn",
        'alias_name': "Lạng Sơn",
        'address': "Lạng Sơn",
        'location': "Tp Lạng Sơn",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=11),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Lạng Sơn - Mẫu Sơn",
        'alias_name': "Mẫu Sơn - Lạng Sơn",
        'address': "Lạng Sơn",
        'location': "Đỉnh Mẫu Sơn",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=11),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Hòa Bình",
        'alias_name': "Hòa Bình",
        'address': "Hòa Bình",
        'location': "Tp Hòa Bình",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=12),
        'area': Area.objects.get(pk=1),
    },
    {
        'name': "Hải Phòng",
        'alias_name': "Hải Phòng",
        'address': "Hải Phòng",
        'location': "Tp Hải Phòng",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=13),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Quảng Ninh Hạ Long",
        'alias_name': "Hạ Long - Quảng Ninh",
        'address': "Quảng Ninh Hạ Long",
        'location': "Tp Hạ Lọng",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=14),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Quảng Ninh Móng Cái",
        'alias_name': "Móng Cái - Quảng Ninh",
        'address': "Quảng Ninh Móng Cái",
        'location': "Tx Móng Cái",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=14),
        'area': Area.objects.get(pk=2),
    },
    {
        'name': "Thái Bình",
        'alias_name': "Thái Bình",
        'address': "Thái Bình",
        'location': "Tp Thái Bình",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=15),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Nam Định",
        'alias_name': "Nam Định",
        'address': "Nam Định",
        'location': "Tp Nam Định",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=16),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Ninh Bình",
        'alias_name': "Ninh Bình",
        'address': "Ninh Bình",
        'location': "Tp Ninh Bình",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=18),
        'area': Area.objects.get(pk=3),
    },
    {
        'name': "Thanh Hóa - Quyết Thắng",
        'alias_name': "Quyết Thắng - Thanh Hóa",
        'address': "Thanh Hóa",
        'location': "Đồi Quyết Thắng",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=19),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Thanh Hóa - Bá Thước",
        'alias_name': "Bá Thước - Thanh Hóa",
        'address': "Thanh Hóa",
        'location': "Đồi Bá Thước",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=19),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Nghệ An",
        'alias_name': "Vinh - Nghệ An",
        'address': "Nghệ An",
        'location': "Tp Vinh",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=20),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Hà Tĩnh - Thiên Tượng",
        'alias_name': "Thiên Tượng - Hà Tĩnh",
        'address': "Hà Tĩnh",
        'location': "Đồi Thiên Tượng",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=21),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Hà Tĩnh",
        'alias_name': "Hà Tĩnh",
        'address': "Hà Tĩnh",
        'location': "Tp Hà Tĩnh",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=21),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Quảng Bình",
        'alias_name': "Đồng Hới - Quảng Bình",
        'address': "Quảng Bình",
        'location': "Tp Đồng Hới",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=22),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Quảng Trị",
        'alias_name': "Đông Hà - Quảng Trị",
        'address': "Quảng Trị",
        'location': "Tp Đông Hà",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=23),
        'area': Area.objects.get(pk=4),
    },
    {
        'name': "Quảng Nam",
        'alias_name': "Tam Kỳ - Quảng Nam",
        'address': "Quảng Nam",
        'location': "Tp Tam Kỳ",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=24),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Quảng Ngãi",
        'alias_name': "Quảng Ngãi",
        'address': "Quảng Ngãi",
        'location': "Tp Quảng Ngãi",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=25),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Bình Định",
        'alias_name': "Quy Nhơn - Bình Định",
        'address': "Bình Định",
        'location': "Núi Vũng Chua",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=26),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Khánh Hòa",
        'alias_name': "Nha Trang - Khánh Hòa",
        'address': "Khánh Hòa",
        'location': "Đồng Đế (VOV)",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=27),
        'area': Area.objects.get(pk=5),
    },
    
    {
        'name': "Ninh Thuận",
        'alias_name': "Phan Rang - Ninh Thuận",
        'address': "Ninh Thuận",
        'location': "Tp Phan Rang",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=28),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Bình Thuận",
        'alias_name': "Phan Thiết - Bình Thuận",
        'address': "Bình Thuận",
        'location': "Tp Phan Thiết",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=29),
        'area': Area.objects.get(pk=5),
    },
    {
        'name': "Kon Tum",
        'alias_name': "Kon Tum",
        'address': "Kon Tum",
        'location': "Tx Kon Tum",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=30),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Gia Lai Hàm Rồng",
        'alias_name': "Playku - Gia Lai",
        'address': "Gia Lai Hàm Rồng",
        'location': "Tp Playcu",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=31),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Đắk Lắk Hà Lan",
        'alias_name': "Hà Lan - Đắk Lắk",
        'address': "Đắk Lắk Hà Lan",
        'location': "Đèo Hà Lan",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=32),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Đắk Lắk BMT",
        'alias_name': "Buôn Ma Thuột - Đắk Lắk",
        'address': "Đắk Lắk BMT",
        'location': "Buôn Ma Thuột",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=32),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Đắk Nông",
        'alias_name': "Gia Nghĩa - Đắk Nông",
        'address': "Đắk Nông",
        'location': "Tx Gia Nghĩa",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=33),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Lâm Đồng Đà Lạt",
        'alias_name': "Đà Lạt - Lâm Đồng",
        'address': "Lâm Đồng Đà Lạt",
        'location': "Tp Đà Lạt",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=34),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Lâm Đồng Cầu Đất",
        'alias_name': "Cầu Đất - Lâm Đồng",
        'address': "Lâm Đồng Cầu Đất",
        'location': "Núi Cầu Đất",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=34),
        'area': Area.objects.get(pk=6),
    },
    {
        'name': "Bình Phước",
        'alias_name': "Bà Rá - Bình Phước",
        'address': "Bình Phước",
        'location': "Núi Bà Rá",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=35),
        'area': Area.objects.get(pk=7),
    },
    {
        'name': "Tây Ninh",
        'alias_name': "Bà Đen - Tây Ninh",
        'address': "Tây Ninh",
        'location': "Núi Bà Đen",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=36),
        'area': Area.objects.get(pk=7),
    },
    {
        'name': "An Giang",
        'alias_name': "Núi Cấm - An Giang",
        'address': "An Giang",
        'location': "Núi Cấm",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=38),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Bến Tre",
        'alias_name': "Bến Tre",
        'address': "Bến Tre",
        'location': "Tx Bến Tre",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=39),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Sóc Trăng",
        'alias_name': "Sóc Trăng",
        'address': "Sóc Trăng",
        'location': "Tx Sóc Trăng",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=40),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Kiên Giang Hà Tiên",
        'alias_name': "Hà Tiên - Kiên Giang",
        'address': "Kiên Giang Hà Tiên",
        'location': "Tx Hà Tiên",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=41),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Kiên Giang Hòn Me",
        'alias_name': "Hòn Me - Kiên Giang",
        'address': "Kiên Giang Hòn Me",
        'location': "Hòn Me",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=41),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Bạc Liêu",
        'alias_name': "Bạc Liêu",
        'address': "Bạc Liêu",
        'location': "Tx Bạc Liêu",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=42),
        'area': Area.objects.get(pk=8),
    },
    {
        'name': "Cà Mau",
        'alias_name': "Cà Mau",
        'address': "Cà Mau",
        'location': "Tp Cà Mau",
        'manage_type': "Hợp đồng", # 1 = Trực tiếp, 0 = Hợp đồng
        'description': "",
        'television': Television.objects.get(pk=43),
        'area': Area.objects.get(pk=8),
    },
]

class BasestaionSeeder():
    def __init__(self):
        Basestation.objects.all().delete()
        for bts in BASESTATIONS:
            new_bts = Basestation(name=bts['name'],
                                  alias_name=bts['alias_name'],
                                  address=bts['address'],
                                  location=bts['location'],
                                  description=bts['description'],
                                  television=bts['television'],
                                  area=bts['area'],)
            new_bts.save()