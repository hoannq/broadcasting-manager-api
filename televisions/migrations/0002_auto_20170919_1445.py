# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 14:45
from __future__ import unicode_literals

from django.db import migrations
from televisions.models import Television

TELEVISIONS = [
    {
        'name': 'TRUNG TÂM KỸ THUẬT TDPS, Đài Truyền hình Việt Nam',
        'province': 'Hà Nội',
        'representative': 'TRẦN QUỐC TUẤN',
        'position': 'P. Giám đốc',
        'address': 'Số 9, Nguyên Hồng, Ba Đình Hà Nội',
        'phone_number': '(04) 3 8317 440',
        'fax': '(04) 3 771 6244',
        'tax_code': '101567589',
        'bank_account': '102010001355996',
        'bank': 'Ngân hàng TMCP Công thương Việt Nam - Chi nhánh Thành phố Hà Nội',
        'decision_number': '2048/QĐ-THVN',
        'decision_date': '2014-11-19',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH HÀ GIANG',
        'province': 'Hà Giang',
        'representative': 'TÔ TUYÊN',
        'position': 'Giám đốc',
        'address': 'Tổ 7 Phường Trần Phú – Thành phố Hà Giang, tỉnh Hà Giang',
        'phone_number': '(0219) 3864 732',
        'fax': '(0219) 3860 043',
        'tax_code': '5100102068',
        'bank_account': '34510000000410',
        'bank': 'Ngân hàng đầu tư và phát triển tỉnh Hà Giang',
        'decision_number': '12/QĐ-UBND',
        'decision_date': '2012-01-04',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH TỈNH LÀO CAI',
        'province': 'Lào Cai',
        'representative': 'PHAN QUANG HƯNG',
        'position': 'Giám đốc',
        'address': 'Đường 30/4 Phường Nam Cường – Thành phố Lào Cai, tỉnh Lào Cai',
        'phone_number': '(020) 3 840093',
        'fax': '(020) 3 3825304',
        'tax_code': '5300140085',
        'bank_account': '37510000000154',
        'bank': 'Ngân hàng Đầu tư & Phát triển tỉnh Lào Cai',
        'decision_number': '2684/QĐ-UBND',
        'decision_date': '2009-08-31',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH TỈNH CAO BẰNG',
        'province': 'Cao Bằng',
        'representative': 'LA VŨ QUANG',
        'position': 'Giám đốc',
        'address': '87 Phố Bế Văn Đàn, Hợp giang, thị xã Cao Bằng',
        'phone_number': '(026) 3852 250',
        'fax': '(026) 3854 022',
        'tax_code': '',
        'bank_account': '102010001447581',
        'bank': 'Ngân hàng TMCP Công thương Việt Nam chi nhánh Cao Bằng',
        'decision_number': '302/QĐUB',
        'decision_date': '1993-11-16',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH ĐIỆN BIÊN',
        'province': 'Điện Biên',
        'representative': 'NGUYỄN NGỌC KỶ',
        'position': 'Giám đốc',
        'address': 'Đường võ nguyên giáp Phường Mường Thanh, thành phố Điện Biên, tỉnh Điện Biên',
        'phone_number': '(0230) 3824 836',
        'fax': '(0230) 3824 035',
        'tax_code': '5600128272',
        'bank_account': '8900211000025',
        'bank': 'Ngân hàng Agribank chi nhánh tỉnh Điện Biên',
        'decision_number': '70/QĐ UBND',
        'decision_date': '1977-04-18',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH LAI CHÂU',
        'province': 'Lai Châu',
        'representative': 'NGUYỄN NGỌC KỶ',
        'position': 'Giám đốc',
        'address': 'Phường Đoàn Kết, Thị xã Lai Châu, Tỉnh Lai Châu',
        'phone_number': '(0231) 3 876 979',
        'fax': '(0231) 3 876 97',
        'tax_code': '6200000304',
        'bank_account': '37130104157600000',
        'bank': 'Kho bạc Nhà nước tỉnh Lai Châu',
        'decision_number': '47/2004/QĐUB',
        'decision_date': '2004-02-25',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH TUYÊN QUANG',
        'province': 'Tuyên Quang',
        'representative': 'MA XUÂN QUANG',
        'position': 'Giám đốc',
        'address': 'Số 219 Đường Tân Trào, Thành phố Tuyên Quang',
        'phone_number': '027 3 822 435',
        'fax': '0273 824 435',
        'tax_code': '5000146449',
        'bank_account': '371221013623',
        'bank': 'Kho bạc Nhà nước tỉnh Tuyên Quang',
        'decision_number': '423/QĐ-UBND',
        'decision_date': '2009-10-26',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH YÊN BÁI',
        'province': 'Yên Bái',
        'representative': 'HÀ MINH ẤT',
        'position': 'Giám đốc',
        'address': 'Số 1, Trần Quốc Toản, phường Đồng Tâm, Thành phố Yên Bái',
        'phone_number': '(029) 3 855 792',
        'fax': '(029) 3853 491',
        'tax_code': '',
        'bank_account': '102010000672377',
        'bank': 'Ngân hàng TMCP Công thương VN - chi nhánh Yên Bái',
        'decision_number': '632/QĐ-UBND',
        'decision_date': '2011-05-09',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH SƠN LA',
        'province': 'Sơn La',
        'representative': 'LÃ MINH TUẤN',
        'position': 'Giám đốc',
        'address': 'Tổ 1, phường Quyết Thắng Thành phố Sơn La',
        'phone_number': '(022)3 853 912',
        'fax': '(022)3 853 559',
        'tax_code': '5500155032',
        'bank_account': '371221018340',
        'bank': 'Kho bạc Nhà nước tỉnh Sơn La',
        'decision_number': '645/QĐ-TC',
        'decision_date': '1977-09-26',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH BẮC KẠN',
        'province': 'Bắc Kạn',
        'representative': 'MA ĐÌNH VIỆT',
        'position': 'Giám đốc',
        'address': 'Phường Phùng Chí Kiên, thị xã Bắc Kạn tỉnh Bắc Kạn',
        'phone_number': '(0281) 3879 753',
        'fax': '(0281) 3871 183',
        'tax_code': '4700113422',
        'bank_account': '102010001534102',
        'bank': 'Ngân hàng Thương mại Cổ phần Công thương Việt Nam - Chi nhánh Bắc Kạn',
        'decision_number': '909/2011',
        'decision_date': '2011-06-01',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH LẠNG SƠN',
        'province': 'Lạng Sơn',
        'representative': 'NÔNG LƯƠNG CHẤN',
        'position': 'Giám đốc',
        'address': 'Số 9 đường Hoàng Văn Thụ, Phường Chi Lăng, Thành phố Lạng Sơn',
        'phone_number': '(025)3 813 531',
        'fax': '(025)3 812 749',
        'tax_code': '',
        'bank_account': '37121106230800000',
        'bank': 'Kho bạc Nhà nước tỉnh Lạng Sơn',
        'decision_number': '217/QĐUB',
        'decision_date': '1991-03-18',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH HÒA BÌNH',
        'province': 'Hoà Bình',
        'representative': 'TÔ DUY NHẤT',
        'position': 'Giám đốc',
        'address': 'Đường Trần Hưng Đạo - Thành  phố Hòa Bình, tỉnh Hòa Bình',
        'phone_number': '(0218) 3 894056',
        'fax': '(0218) 3 852743',
        'tax_code': '5400103506',
        'bank_account': '45510000317006',
        'bank': 'Ngân hàng TMCP Đầu tư & phát triển - chi nhánh Hòa Bình',
        'decision_number': '40575',
        'decision_date': '2011-03-21',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH THÀNH PHỐ HẢI PHÒNG',
        'province': 'Thành phố Hải Phòng',
        'representative': 'ĐOÀN VĂN CHƯƠNG',
        'position': 'Giám đốc',
        'address': '199 Tô Hiệu, quận Lê Chân, thành phố Hải Phòng',
        'phone_number': '(031)3 610 599',
        'fax': '(031)3 846 838',
        'tax_code': '',
        'bank_account': '102010001013100',
        'bank': 'Ngân hàng TMCP Công thương Việt Nam - Chi nhánh Tô Hiệu, Hải Phòng',
        'decision_number': '',
        'decision_date': '',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH QUẢNG NINH',
        'province': 'Quảng Ninh',
        'representative': '',
        'position': 'Giám đốc',
        'address': 'Phường Hồng Hải - Thành phố Hạ Long',
        'phone_number': '(033) 3 825 363',
        'fax': '(033) 3 827 507',
        'tax_code': '',
        'bank_account': '37131044593',
        'bank': 'Kho bạc Nhà nước tỉnh Quảng Ninh',
        'decision_number': '',
        'decision_date': '',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH THÁI BÌNH',
        'province': 'Thái Bình',
        'representative': 'VŨ ANH THAO',
        'position': 'Giám đốc',
        'address': 'Phường Hoàng Diệu, Thành phố Thái Bình, tỉnh Thái Bình',
        'phone_number': '(036) 3 745416',
        'fax': '(036)3 748 263',
        'tax_code': '1000215536',
        'bank_account': '102010000358312',
        'bank': 'Ngân hàng TMCP Công Thương Việt Nam chi nhánh Thái Bình',
        'decision_number': '72/2004/QĐ-UBND',
        'decision_date': '2004-07-22',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH NAM ĐỊNH',
        'province': 'Nam Định',
        'representative': 'TRỊNH XUÂN LỘC',
        'position': 'Giám đốc',
        'address': '255 đường Hàn Thuyên, Thành phố Nam Định, tỉnh Nam Định',
        'phone_number': '(0350) 3643 485',
        'fax': '(0350) 3643 077',
        'tax_code': '',
        'bank_account': '37130109458700000',
        'bank': 'Kho bạc Nhà nước tỉnh Nam Định',
        'decision_number': '',
        'decision_date': '',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH HÀ NAM',
        'province': 'Hà Nam',
        'representative': 'TRỊNH NGÂN LIÊN',
        'position': 'Giám đốc',
        'address': 'Phường Hai Bà Trưng, Thị xã Phủ Lý, tỉnh Hà Nam',
        'phone_number': '(0351) 3851 780',
        'fax': '(0351) 3854 460',
        'tax_code': '',
        'bank_account': '37121066908',
        'bank': 'Kho bạc Nhà nước tỉnh Hà Nam',
        'decision_number': '',
        'decision_date': '',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH NINH BÌNH',
        'province': 'Ninh Bình',
        'representative': 'HOÀNG TUẤN DŨNG',
        'position': 'Giám đốc',
        'address': 'Phố 10, phường Đông Thành, thị xã Ninh Bình',
        'phone_number': '(030) 3 889 357',
        'fax': '(030) 3 875 513',
        'tax_code': '2700139353',
        'bank_account': '371321004241',
        'bank': 'Kho bạc Nhà nước tỉnh Ninh Bình',
        'decision_number': '2798/QĐ - UBND',
        'decision_date': '2007-12-10',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH THANH HOÁ',
        'province': 'Thanh Hoá',
        'representative': 'LÊ HOÀI CHÂU',
        'position': 'Giám đốc',
        'address': 'Số 8 đường Hạc Thành, thành phố Thanh Hoá',
        'phone_number': '(037) 3856 293',
        'fax': '(037) 3857 159',
        'tax_code': '2800230447',
        'bank_account': '3500431101001500',
        'bank': 'Ngân hàng NN & PTNT tỉnh Thanh Hoá',
        'decision_number': '3188/2002',
        'decision_date': '2012-08-23',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH NGHỆ AN',
        'province': 'Nghệ An',
        'representative': 'NGUYỄN NHƯ KHÔI',
        'position': 'Giám đốc',
        'address': 'Số 1 Nguyễn Thị Minh Khai, Thành phố Vinh',
        'phone_number': '(038) 3 598457',
        'fax': '(038) 3 844700',
        'tax_code': '2900325815',
        'bank_account': '102010000485306',
        'bank': 'Ngân hàng công thương Bến Thủy',
        'decision_number': '61/2012/QĐ-UB.TC',
        'decision_date': '2012-08-23',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH HÀ TĨNH',
        'province': 'Hà Tĩnh',
        'representative': 'ĐINH VĂN THIỀM',
        'position': 'Giám đốc',
        'address': 'Số 22 Phan Đình Phùng, Thành phố Hà Tĩnh',
        'phone_number': '(039) 3 855 540',
        'fax': '(039) 3 857 410',
        'tax_code': '',
        'bank_account': '201000586888',
        'bank': 'Ngân hàng TMCP Ngoại thương Hà Tĩnh',
        'decision_number': '999/2002/QĐ-UB-TC',
        'decision_date': '2002-05-09',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH QUẢNG BÌNH',
        'province': 'Quảng Bình',
        'representative': 'LÊ KHÁNH HÒA',
        'position': 'Giám đốc',
        'address': '54 Quang Trung, Thành phố Đồng Hới, tỉnh Quảng Bình',
        'phone_number': '(052) 3 822 522',
        'fax': '(052) 3 822 102',
        'tax_code': '',
        'bank_account': '37130102058900',
        'bank': 'Kho bạc Nhà nước Quảng Bình',
        'decision_number': '167/QĐUB',
        'decision_date': '1993-03-08',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH QUẢNG TRỊ',
        'province': 'Quảng Trị',
        'representative': 'TRẦN ĐỨC HỮU',
        'position': 'Giám đốc',
        'address': 'Phường 1, thành phố Đông Hà, tỉnh Quảng Trị',
        'phone_number': '(053)3 850 509',
        'fax': '(053) 3850 516',
        'tax_code': '',
        'bank_account': '102010000508087',
        'bank': 'Ngân hàng Công thương Quảng Trị',
        'decision_number': '07/QĐUB',
        'decision_date': '2011-04-14',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH QUẢNG NAM',
        'province': 'Quảng Nam',
        'representative': 'MAI VĂN TƯ',
        'position': 'Giám đốc',
        'address': '58 Hùng Vương Tam Kỳ tỉnh Quảng Nam',
        'phone_number': '(0510) 384 5340',
        'fax': '(0510) 3852 401',
        'tax_code': '',
        'bank_account': '651000623899',
        'bank': 'Ngân hàng VCB Quảng Nam',
        'decision_number': '04/2011/QĐUB',
        'decision_date': '2004-02-09',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH QUẢNG NGÃI',
        'province': 'Quảng Ngãi',
        'representative': 'TRƯƠNG QUANG TẤN',
        'position': 'Phó Giám đốc',
        'address': 'Số 165 đại lộ Hùng Vương, thành phố Quảng Ngãi',
        'phone_number': '(055) 3 822 051',
        'fax': '(055) 3 825 420',
        'tax_code': '',
        'bank_account': '371321082709',
        'bank': 'Kho bạc Nhà nước tỉnh Quảng Ngãi',
        'decision_number': '113/2002/QĐUB',
        'decision_date': '2002-10-01',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH BÌNH ĐỊNH',
        'province': 'Bình Định',
        'representative': 'PHẠM VĨNH THÁI',
        'position': 'Giám đốc',
        'address': '23 Mai Xuân Thưởng Quy Nhơn tỉnh Bình Định',
        'phone_number': '(056) 3822 878',
        'fax': '(056) 3824 718',
        'tax_code': '4100259331',
        'bank_account': '51000323365',
        'bank': 'Ngân hàng Ngoại thương Quy Nhơn',
        'decision_number': '738/QĐ-UBND',
        'decision_date': '2008-12-26',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH KHÁNH HOÀ',
        'province': 'Khánh Hoà',
        'representative': 'TRƯƠNG TẤN MINH',
        'position': 'Giám đốc',
        'address': 'Số 70 Trần Phú, Thành phố Nha Trang, tỉnh Khánh Hoà',
        'phone_number': '(058) 3 525 959',
        'fax': '(058) 3523 158',
        'tax_code': '',
        'bank_account': '37121021454',
        'bank': 'Kho bạc Nhà nước tỉnh Khánh Hoà',
        'decision_number': '2575/QĐUB',
        'decision_date': '1994-11-22',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH NINH THUẬN',
        'province': 'Ninh Thuận',
        'representative': 'NGUYỄN MINH HÀ',
        'position': 'Giám đốc',
        'address': '285A đường 21/8, Phước Mỹ, Thị xã Phan Rang, Ninh Thuận',
        'phone_number': '(068) 823 759',
        'fax': '(068) 831 177',
        'tax_code': '',
        'bank_account': '61510000004474',
        'bank': 'Ngân hàng TMCP Đầu tư và phát triển Việt Nam – Chi nhánh tỉnh Ninh Thuận',
        'decision_number': '186/2004/QĐ-UB',
        'decision_date': '2004-11-15',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH BÌNH THUẬN',
        'province': 'Bình Thuận',
        'representative': 'LÊ VĂN BẢY',
        'position': 'Giám đốc',
        'address': '339/ 341 Thủ khoa Huân- T.p Phan Thiết - tỉnh Bình Thuận',
        'phone_number': '(062) 3 833 409',
        'fax': '(062) 3 835 781',
        'tax_code': '3400189122',
        'bank_account': '371301020103',
        'bank': 'Kho bạc Nhà nước tỉnh Bình Thuận',
        'decision_number': '3455/QĐUB',
        'decision_date': '2006-12-28',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH KON TUM',
        'province': 'Kon Tum',
        'representative': 'PHAN CƯ',
        'position': 'Giám đốc',
        'address': 'Số 258A Phan Đình Phùng, Thành phố Kon Tum, tỉnh Kon Tum',
        'phone_number': '(060) 3 866261',
        'fax': '(060) 3 866261',
        'tax_code': '6100108713',
        'bank_account': '371301037641',
        'bank': 'Kho bạc Nhà nước tỉnh Kon Tum',
        'decision_number': '30',
        'decision_date': '1991-11-30',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH GIA LAI',
        'province': 'Gia Lai',
        'representative': 'ĐỖ NGỌC KỲ',
        'position': 'Giám đốc',
        'address': 'Số 1 Đường Lý Thái Tổ - Thành phố Pleiku tỉnh Gia Lai',
        'phone_number': '(059) 3 824222',
        'fax': '(059) 3 716659',
        'tax_code': '59001809891',
        'bank_account': '291000252292',
        'bank': 'Ngân hàng Ngoại thương Gia Lai',
        'decision_number': '27/2009/QĐ-UB',
        'decision_date': '2009-08-21',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH ĐẮK LẮK',
        'province': 'Đắk Lắk',
        'representative': 'TÔ THANH BÌNH',
        'position': 'Giám đốc',
        'address': 'Số 01 Nguyễn Tất Thành, thành phố Buôn Mê Thuột',
        'phone_number': '(050) 3852 544',
        'fax': '(050) 3810 375',
        'tax_code': '',
        'bank_account': '5214201000860',
        'bank': 'Ngân hàng Nông nghiệp và phát triển nông thôn tỉnh tỉnh Đắk Lắk – chi nhánh Phan Chu Trinh',
        'decision_number': '241/QĐUB',
        'decision_date': '2009-02-06',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH ĐẮK NÔNG',
        'province': 'Đắc Nông',
        'representative': 'HÀ TRUNG KÝ',
        'position': 'Giám đốc',
        'address': 'Thị xã Gia Nghĩa, tỉnh Đắc Nông',
        'phone_number': '(050) 3543 866',
        'fax': '(050) 3543 866',
        'tax_code': '',
        'bank_account': '102010001399736',
        'bank': 'Ngân hàng TMCP Công thương Việt Nam – Chi nhánh Đắc Nông',
        'decision_number': '1987/QĐ-UBND',
        'decision_date': '2010-12-08',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH LÂM ĐỒNG',
        'province': 'Lâm Đồng',
        'representative': 'NGUYỄN THANH NHÂN',
        'position': 'Giám đốc',
        'address': 'Số 10 Trần Hưng Đạo, Thành phố Đà Lạt',
        'phone_number': '(063) 3 820 875',
        'fax': '(063) 3 829 510',
        'tax_code': '5800075927',
        'bank_account': '5400211000760',
        'bank': 'Ngân hàng Nông nghiệp và phát triển nông thôn tỉnh Lâm Đồng',
        'decision_number': '32/2011/QĐ UBND',
        'decision_date': '2011-06-23',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH BÌNH PHƯỚC',
        'province': 'Bình Phước',
        'representative': 'PHAN MINH HOÀNG',
        'position': 'Giám đốc',
        'address': 'Số 1, Đường Trần Hưng Đạo, phường Tân Phú, thị xã Đồng Xoài, tỉnh Bình Phước',
        'phone_number': '(0651) 388 7062',
        'fax': '(0651) 387 0720',
        'tax_code': '3800101316',
        'bank_account': '65510000008520',
        'bank': 'Ngân hàng Đầu tư và phát triển Bình Phước',
        'decision_number': '113/2005/QĐ-UBND',
        'decision_date': '2005-09-29',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH TÂY NINH',
        'province': 'Tây Ninh',
        'representative': 'NGUYỄN NAM GIANG',
        'position': 'Giám đốc',
        'address': 'Số 322, đường 30/4, Phường 3 Thành phố Tây Ninh',
        'phone_number': '(066) 3828 781',
        'fax': '(066) 3820 970',
        'tax_code': '',
        'bank_account': '934020000130',
        'bank': 'Kho bạc Nhà nước tỉnh Tây Ninh',
        'decision_number': '20',
        'decision_date': '2011-06-29',
        'description': ''
    },
    {
        'name': 'ĐÀI TRUYỀN HÌNH THÀNH PHỐ HỒ CHÍ MINH',
        'province': 'Thành phố Hồ Chí Minh',
        'representative': 'NGUYỄN QUÝ HÒA',
        'position': 'Tổng Giám đốc',
        'address': 'Số 14 Phố Đinh Tiên Hoàng, quận 1, Thành phố Hồ Chí Minh',
        'phone_number': '(08) 39102 354',
        'fax': '(08) 39102 354',
        'tax_code': '',
        'bank_account': '945020025003',
        'bank': 'Kho bạc Nhà nước Thành phố Hồ chí Minh',
        'decision_number': '15/2007/QĐ-UBND',
        'decision_date': '2007-02-02',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH AN GIANG',
        'province': 'An Giang',
        'representative': 'CAO QUANG LIÊM',
        'position': 'Giám đốc',
        'address': '45/1 Trần Hưng Đạo, Phường Bình Khánh Thành phố Long Xuyên',
        'phone_number': '(076) 3 852342',
        'fax': '(076) 3 956100',
        'tax_code': '16003539471',
        'bank_account': '70110000052675',
        'bank': 'Ngân hàng Đầu tư và Phát triển Việt Nam - Chi nhánh An Giang',
        'decision_number': '43/2009/QĐ-UBND',
        'decision_date': '2009-09-25',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH BẾN TRE',
        'province': 'Bến Tre',
        'representative': 'TRẦN VĂN HỮU',
        'position': 'Giám đốc',
        'address': '1/3 Trần Quốc Tuấn, phường 4, Thành phố Bến Tre',
        'phone_number': '(075) 3822 248 (106)',
        'fax': '(075) 3825 787',
        'tax_code': '1300109296',
        'bank_account': '72110000094770',
        'bank': 'Ngân hàng đầu tư và phát triển Bến Tre',
        'decision_number': '4131/2007/QĐ-UBND',
        'decision_date': '2005-11-28',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH SÓC TRĂNG',
        'province': 'Sóc Trăng',
        'representative': 'LÂM THỊ LỆ PHƯƠNG',
        'position': 'Giám đốc',
        'address': 'Đường 132 Trần Văn Bảy, phường 3, Thành phố Sóc Trăng',
        'phone_number': '(079) 3826 765',
        'fax': '(079) 3825 876',
        'tax_code': '',
        'bank_account': '371221042820',
        'bank': 'Kho bạc Nhà nước Sóc Trăng',
        'decision_number': '',
        'decision_date': '',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH KIÊN GIANG',
        'province': 'Kiên Giang',
        'representative': 'NGUYỄN THANH CAO',
        'position': 'Giám đốc',
        'address': 'Số 39 Đống Đa Vĩnh Lạc Thành phố Rạch Giá tỉnh Kiên Giang',
        'phone_number': '(077) 3927 066',
        'fax': '(077) 3813 990',
        'tax_code': '',
        'bank_account': '1003546997',
        'bank': 'Ngân hàng SHB Kiên Giang',
        'decision_number': '',
        'decision_date': '',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH BẠC LIÊU',
        'province': 'Bạc Liêu',
        'representative': 'LÊ HỮU BUÔL',
        'position': 'Giám đốc',
        'address': '410 Đường 23/8 Phường 8, Thành phố Bạc Liêu',
        'phone_number': '(0781) 3825 397',
        'fax': '(0781) 3823 989',
        'tax_code': '1900137231',
        'bank_account': '102010001557655',
        'bank': 'Ngân hàng TMCP Công thương tỉnh Bạc Liêu',
        'decision_number': '25/QĐUB',
        'decision_date': '2010-12-31',
        'description': ''
    },
    {
        'name': 'ĐÀI PTTH CÀ MAU',
        'province': 'Cà Mau',
        'representative': 'ĐỖ KIẾN QUỐC',
        'position': 'Giám đốc',
        'address': '413 Nguyễn Trãi, Phường 9, Thành phố Cà Mau',
        'phone_number': '(0780) 3831 664',
        'fax': '(0780) 3833 621',
        'tax_code': '',
        'bank_account': '102010000327479',
        'bank': 'Ngân hàng công thương tỉnh Cà Mau',
        'decision_number': '58/QĐUB',
        'decision_date': '1997-01-01',
        'description': ''
    }
]


def load_televisions(apps, schema_editor):
    for television in TELEVISIONS:
        new_television = Television(name=television['name'],
                                    province=television['province'],
                                    representative=television['representative'],
                                    position=television['position'],
                                    address=television['address'],
                                    phone_number=television['phone_number'],
                                    fax=television['fax'],
                                    tax_code=television['tax_code'],
                                    bank_account=television['bank_account'],
                                    bank=television['bank'],
                                    decision_number=television['decision_number'],
                                    decision_date=television['decision_date'],
                                    description=television['description'])
        new_television.save()

def delete_televisions(apps, schema_editor):
    Television.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('televisions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_televisions, delete_televisions),
    ]
