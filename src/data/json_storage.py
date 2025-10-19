from src.data import IStorage


class JSONStorage(IStorage):
    """
    Lớp lưu trữ dữ liệu nhân viên dưới định dạng JSON.
    Kế thừa từ giao diện IStorage và triển khai các phương thức lưu và đọc dữ liệu.
    """

    def save(self, file_path: str, employees: list):
        """Lưu danh sách nhân viên vào một file JSON."""
        pass

    def load(self, file_path: str) -> list:
        """Đọc danh sách nhân viên từ file JSON."""
        pass