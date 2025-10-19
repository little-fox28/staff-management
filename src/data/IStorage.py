from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Interface (giao diện) này định nghĩa một hợp đồng (contract) cho các lớp lưu trữ dữ liệu.
    Bất kỳ lớp nào muốn hoạt động như một cơ chế lưu trữ (ví dụ: lưu vào file CSV, JSON, hoặc cơ sở dữ liệu)
    phải triển khai (implement) tất cả các phương thức được định nghĩa trong interface này.

    Điều này giúp đảm bảo tính nhất quán và cho phép dễ dàng thay đổi phương thức lưu trữ
    mà không cần thay đổi logic nghiệp vụ của ứng dụng.
    """
    @abstractmethod
    def save(self, file_path: str, employees: list):
        """Lưu danh sách nhân viên vào một file."""
        pass

    @abstractmethod
    def load(self, file_path: str) -> list:
        """Đọc danh sách nhân viên từ file."""
        pass