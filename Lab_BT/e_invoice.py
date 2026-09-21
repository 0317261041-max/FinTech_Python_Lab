

ten_sp = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))

# Tính tiền
tong_tien_hang = so_luong * don_gia
thue_vat = tong_tien_hang * 0.08
tong_thanh_toan = tong_tien_hang + thue_vat

# In hóa đơn
print("\n========== HÓA ĐƠN BÁN HÀNG ==========")
print(f"Tên sản phẩm: {ten_sp}")
print(f"Số lượng: {so_luong}")
print(f"Đơn giá: {don_gia:,.0f} VND")
print(f"Tổng tiền hàng: {tong_tien_hang:,.0f} VND")
print(f"Thuế VAT (8%): {thue_vat:,.0f} VND")
print(f"Tổng thanh toán: {tong_thanh_toan:,.0f} VND")
