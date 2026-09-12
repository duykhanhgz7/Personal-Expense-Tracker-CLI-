import sqlite3

# 1. Kết nối đến cơ sở dữ liệu (nếu chưa có, Python sẽ tự tạo một file tên là 'chi_tieu.db')
conn = sqlite3.connect('chi_tieu.db')
cursor = conn.cursor()

# 2. Tạo bảng lưu trữ giao dịch (nếu bảng chưa tồn tại)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS giao_dich (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        so_tien REAL,
        danh_muc TEXT
    )
''')
conn.commit()

confirmation = input("Bạn có muốn nhập dữ liệu chi tiêu mới không? (y/n): ")
while confirmation.lower() == 'y':
    # 3. Nhập dữ liệu từ bàn phím
    so_tien = float(input("Nhập số tiền chi: "))
    danh_muc = input("Nhập danh mục (ví dụ: Ăn uống, Đi lại): ")

    # 4. Lưu dữ liệu vào cơ sở dữ liệu
    cursor.execute("INSERT INTO giao_dich (so_tien, danh_muc) VALUES (?, ?)", (so_tien, danh_muc))
    conn.commit()
    confirmation = input("Bạn có muốn nhập dữ liệu chi tiêu mới không? (y/n): ")

# Đóng kết nối
conn.close()

print("Đã lưu thành công vào cơ sở dữ liệu!")