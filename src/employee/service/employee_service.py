from src.employee.employee import Employee


class EmployeeService:
    """
    Lớp này thực hiện các logic nghiệp vụ về Nhân sự của ứng dụng
    """


    def add_employee(self, employee_data: dict):
        """
        Adds a new employee.
        Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.
        """
        print(f"Adding employee with data: {employee_data}")
        # Logic to create and save employee will be implemented here.
        pass

    def get_all_employees(self) -> list[Employee]:
        """
        Returns all employees.
        Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.
        """
        print("Getting all employees")
        # Logic to read employees from file will be implemented here.
        return []

    def find_employee_by_id(self, employee_id: str) -> Employee | None:
        """
        Finds an employee by their ID.
        Y3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.
        """
        print(f"Finding employee with ID: {employee_id}")
        # Logic to find employee will be implemented here.
        return None

    def delete_employee_by_id(self, employee_id: str):
        """
        Deletes an employee by their ID.
        Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.
        """
        print(f"Deleting employee with ID: {employee_id}")
        # Logic to delete employee will be implemented here.
        pass

    def update_employee(self, employee_id: str, new_data: dict):
        """
        Updates an employee's information.
        Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.
        """
        print(f"Updating employee {employee_id} with data: {new_data}")
        # Logic to update employee will be implemented here.
        pass

    def find_employees_by_salary_range(self, min_salary: float, max_salary: float) -> list[Employee]:
        """
        Finds employees within a given salary range.
        Y6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.
        """
        print(f"Finding employees with salary between {min_salary} and {max_salary}")
        # Logic to find employees by salary will be implemented here.
        return []

    def sort_employees_by_name(self) -> list[Employee]:
        """
        Sorts employees by their full name.
        Y7. Sắp xếp nhân viên theo họ và tên.
        """
        print("Sorting employees by name")
        # Logic to sort employees by name will be implemented here.
        return []

    def sort_employees_by_income(self) -> list[Employee]:
        """
        Sorts employees by their income.
        Y8. Sắp xếp nhân viên theo thu nhập.
        """
        print("Sorting employees by income")
        # Logic to sort employees by income will be implemented here.
        return []

    def get_top_5_employees_by_income(self) -> list[Employee]:
        """
        Gets the top 5 employees with the highest income.
        Y9. Xuất 5 nhân viên có thu nhập cao nhất.
        """
        print("Getting top 5 employees by income")
        # Logic to get top 5 employees will be implemented here.
        return []

