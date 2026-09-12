import sqlite3

def khoi_tao_db():
    conn = sqlite3.connect('chi_tieu.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS giao_dich (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            so_tien REAL,
            danh_muc TEXT
        )
    ''')
    conn.commit()
    conn.close()

def main():
    khoi_tao_db()
    
    while True:
        print("\n--- QUẢN LÝ CHI TIÊU CÁ NHÂN ---")
        print("1. Thêm giao dịch mới")
        print("2. Xem lịch sử chi tiêu")
        print("3. Lọc theo danh mục")
        print("4. Thoát chương trình")
        
        lua_chon = input("Chọn chức năng (1-4): ")
        
        if lua_chon == '1':
            conn = sqlite3.connect('chi_tieu.db')
            cursor = conn.cursor()
            so_tien = float(input("Nhập số tiền chi: "))
            danh_muc = input("Nhập danh mục (ví dụ: Ăn uống, Đi lại): ")
            cursor.execute("INSERT INTO giao_dich (so_tien, danh_muc) VALUES (?, ?)", (so_tien, danh_muc))
            conn.commit()
            conn.close()
            print("Đã lưu thành công!")
            
        elif lua_chon == '2':
            conn = sqlite3.connect('chi_tieu.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM giao_dich")
            danh_sach = cursor.fetchall()
            print("\n--- LỊCH SỬ CHI TIÊU ---")
            for row in danh_sach:
                print(f"ID: {row[0]} | Số tiền: {row[1]:,.0f} VNĐ | Danh mục: {row[2]}")
            conn.close()
            
        elif lua_chon == '3':
            conn = sqlite3.connect('chi_tieu.db')
            cursor = conn.cursor()
            tu_khoa = input("Nhập tên danh mục cần lọc: ")
            cursor.execute("SELECT id, so_tien, danh_muc FROM giao_dich WHERE danh_muc LIKE ?", ('%' + tu_khoa + '%',))
            ket_qua = cursor.fetchall()
            print(f"\n--- KẾT QUẢ CHO: '{tu_khoa}' ---")
            tong_tien = sum(row[1] for row in ket_qua)
            for row in ket_qua:
                print(f"ID: {row[0]} | Số tiền: {row[1]:,.0f} VNĐ | Danh mục: {row[2]}")
            print(f"--> Tổng chi: {tong_tien:,.0f} VNĐ")
            conn.close()
            
        elif lua_chon == '4':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 đến 4.")

if __name__ == "__main__":
    main()
