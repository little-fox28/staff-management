
# Cấu trúc dự án Quản lý nhân viên

Dưới đây là sơ đồ cấu trúc thư mục của dự án cùng với giải thích chi tiết bằng tiếng Việt.

```
staff-management/
├── .gitignore                      # Các file và thư mục được Git bỏ qua
├── CONTRIBUTING.md                 # Hướng dẫn đóng góp cho dự án
├── project_structure.md            # File này, mô tả cấu trúc dự án
├── README.md                       # File giới thiệu tổng quan về dự án
├── .idea/                          # Thư mục cài đặt của IDE (ví dụ: PyCharm)
└── src/                            # Thư mục chứa mã nguồn chính
    ├── __init__.py                 # Đánh dấu thư mục `src` là một Python package
    ├── main.py                     # Điểm khởi đầu của ứng dụng
    ├── data_handler/               # Gói xử lý việc đọc/ghi dữ liệu từ các nguồn khác nhau
    │   ├── __init__.py
    │   ├── IStorage.py             # Interface (giao diện) cho các lớp lưu trữ dữ liệu
    │   ├── csv_storage.py          # Logic lưu trữ dữ liệu dưới dạng file CSV
    │   ├── json_storage.py         # Logic lưu trữ dữ liệu dưới dạng file JSON
    │   ├── txt_storage.py          # Logic lưu trữ dữ liệu dưới dạng file text
    │   └── xml_storage.py          # Logic lưu trữ dữ liệu dưới dạng file XML
    ├── database/                   # Thư mục chứa các file dữ liệu (nếu có)
    │   └── DUMMY_DATA              # Ví dụ về file dữ liệu
    ├── employee/                   # Gói chứa mọi thứ liên quan đến nhân viên
    │   ├── __init__.py
    │   ├── employee.py             # Định nghĩa lớp `Employee` cơ sở
    │   ├── role/                   # Gói con chứa các vai trò (chức vụ) khác nhau
    │   │   ├── __init__.py
    │   │   ├── adminstrative.py    # Định nghĩa vai trò nhân viên hành chính
    │   │   ├── HOD.py              # Định nghĩa vai trò Trưởng phòng (Head of Department)
    │   │   └── sales.py            # Định nghĩa vai trò nhân viên kinh doanh
    │   └── service/                # Gói chứa các logic nghiệp vụ liên quan đến nhân viên
    │       ├── IEmployee_service.py # Interface cho dịch vụ quản lý nhân viên
    │       └── employee_service.py # Lớp triển khai logic quản lý nhân viên
    ├── menu/                       # Gói chứa các module liên quan đến giao diện người dùng
    │   ├── __init__.py
    │   ├── menu_handler.py         # Chứa logic xử lý các lựa chọn từ menu
    │   └── menu_ui.py              # Chứa code để hiển thị menu cho người dùng
    └── utils/                      # Gói chứa các hàm tiện ích dùng chung
        └── id_generator.py         # Tiện ích tạo ID duy nhất cho nhân viên
```

## Ghi chú chi tiết

*   **`.gitignore`**: Rất quan trọng để không đưa các file không cần thiết (như file của IDE, file cache của Python) vào repository.
*   **`src/`**: Tách biệt mã nguồn khỏi các file cấu hình ở gốc dự án giúp cấu trúc rõ ràng hơn.
*   **`main.py`**: Là file bạn sẽ chạy để khởi động chương trình. Nó sẽ điều phối và gọi các module khác.
*   **Gói `data_handler`**: Chứa logic để trừu tượng hóa việc lưu trữ dữ liệu. `IStorage` định nghĩa một "hợp đồng" chung, và các lớp khác (`csv_storage`, `json_storage`) triển khai "hợp đồng" đó.
*   **Gói `employee`**:
    *   **`service`**: Tách logic nghiệp vụ (cách thêm, sửa, xóa nhân viên) ra khỏi các phần khác. `IEmployee_service` là một interface giúp cho việc thay thế hoặc mở rộng logic này dễ dàng hơn.
    *   **`role`**: Chia các vai trò thành các file riêng biệt giúp dễ quản lý và mở rộng.
*   **Gói `menu`**:
    *   Tách biệt `menu_ui.py` (giao diện) và `menu_handler.py` (xử lý) là một thực hành tốt. Nó giúp bạn có thể thay đổi giao diện mà không ảnh hưởng đến logic nghiệp vụ và ngược lại.
*   **Gói `utils`**: Chứa các hàm nhỏ, có thể tái sử dụng ở nhiều nơi trong dự án.
