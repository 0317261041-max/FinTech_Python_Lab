
# Bài 3: Giao diện nhập liệu và xuất thẻ hội viên FinTech
# Chuẩn hóa dữ liệu đầu vào theo chuẩn PEP 8
print("=== HỆ THỐNG ĐĂNG KÝ HỘI VIÊN MỚI ===")
# 1. Nhận dữ liệu đầu vào từ bàn phím
ho_ten_raw = input("Nhập họ và tên khách hàng: ")
tuoi_input = input("Nhập tuổi khách hàng: ")
ma_kh_raw = input("Nhập mã khách hàng (VD: ft1001): ")
# 2. Xử lý và chuẩn hóa dữ liệu
# .strip() để loại bỏ khoảng trắng thừa ở đầu/cuối chuỗi
# .title() để viết hoa chữ cái đầu mỗi từ trong họ tên
ho_ten_chuan = ho_ten_raw.strip().title()
# .upper() để chuyển toàn bộ mã khách hàng thành chữ in hoa
ma_kh_chuan = ma_kh_raw.strip().upper()
# Ép kiểu dữ liệu tuổi từ dạng Chuỗi (String) sang Số nguyên (Integer)
tuoi = int(tuoi_input)
# 3. In thẻ hội viên bằng F-string
print("\n" + "=" * 45)
print(" THẺ HỘI VIÊN FINTECH CHÍNH THỨC ")
print("=" * 45)
print(f"Mã số hội viên : {ma_kh_chuan}")
print(f"Họ và tên : {ho_ten_chuan}")
print(f"Tuổi : {tuoi} tuổi")
print(f"Hạng tài khoản : Standard Member")
print(f"Trạng thái : Đã kích hoạt")
print("=" * 45)
print("Cảm ơn quý khách đã gia nhập hệ thống số!")
