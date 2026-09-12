import sqlite3

# Kết nối lại tới file cơ sở dữ liệu đã có
conn = sqlite3.connect('chi_tieu.db')
cursor = conn.cursor()

# Lấy toàn bộ dữ liệu từ bảng giao_dich
cursor.execute("SELECT * FROM giao_dich")
danh_sach = cursor.fetchall()

# Hiển thị danh sách ra màn hình
print("\n--- LỊCH SỬ CHI TIÊU CỦA BẠN ---")
for row in danh_sach:
    ma_giao_dich, so_tien, danh_muc = row
    print(f"ID: {ma_giao_dich} | Số tiền: {so_tien:,.0f} VNĐ | Danh mục: {danh_muc}")

# Lọc ra các danh mục duy nhất (không bị trùng lặp) đã lưu
cursor.execute("SELECT DISTINCT danh_muc FROM giao_dich")
danh_muc_list = cursor.fetchall()

# Hiển thị danh sách các danh mục
print("\n--- CÁC DANH MỤC BẠN ĐÃ DÙNG ---")
for row in danh_muc_list:
    print(f"- {row[0]}")

# Nhập danh mục bạn muốn lọc
tu_khoa = input("Nhập tên danh mục bạn muốn lọc (ví dụ: Ăn uống): ")

# Truy vấn các giao dịch có chứa danh mục tương ứng
cursor.execute("SELECT id, so_tien, danh_muc FROM giao_dich WHERE danh_muc LIKE ?", ('%' + tu_khoa + '%',))
ket_qua = cursor.fetchall()

# Hiển thị kết quả lọc
print(f"\n--- KẾT QUẢ LỌC CHO DANH MỤC: '{tu_khoa}' ---")
if len(ket_qua) == 0:
    print("Không tìm thấy giao dịch nào trong danh mục này.")
else:
    tong_tien = 0
    for row in ket_qua:
        ma_giao_dich, so_tien, danh_muc = row
        print(f"ID: {ma_giao_dich} | Số tiền: {so_tien:,.0f} VNĐ | Danh mục: {danh_muc}")
        tong_tien += so_tien
    print(f"--> Tổng chi cho danh mục này: {tong_tien:,.0f} VNĐ")

# Đóng kết nối
conn.close()