from src.data_handler import IStorage


class TXTStorage(IStorage):
    """
    Lớp lưu trữ dữ liệu nhân viên dưới định dạng TXT.
    Kế thừa từ giao diện IStorage và triển khai các phương thức lưu và đọc dữ liệu.
    """

    def save(self, file_path: str, employees: list):
        """Lưu danh sách nhân viên vào một file TXT."""
        pass

    def load(self, file_path: str) -> list:
        """Đọc danh sách nhân viên từ file TXT."""
        pass