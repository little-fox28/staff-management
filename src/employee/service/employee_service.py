from src.employee.employee import Employee
from src.employee.role.adminstrative import AdminStaff
from src.employee.role.sales import SalesStaff
from src.employee.role.HOD import HOD
from src.employee.service.IEmployee_service import IEmployeeService
from src.utils.id_generator import generate_unique_id


def _create_employee_from_data(employee_data: dict) -> Employee:
    emp_type = employee_data.get('type')
    employee = None

    if emp_type == 'SAL':
        employee = SalesStaff(
            emp_id=employee_data['id'],
            full_name=employee_data['full_name'],
            basic_salary=employee_data['basic_salary'],
            sales_amount=employee_data.get('sales_amount', 0.0),
            commission_rate=employee_data.get('commission_rate', 0.0)
        )
    elif emp_type == 'ADM':
        employee = AdminStaff(
            emp_id=employee_data['id'],
            full_name=employee_data['full_name'],
            basic_salary=employee_data['basic_salary']
        )
    else:
        raise ValueError(f"Invalid employee type: {emp_type}")

    if employee_data.get('role') == 'HOD':
        employee = HOD(employee, responsibility_salary=employee_data.get('responsibility_salary', 0.0))

    return employee


class EmployeeService(IEmployeeService):
    def __init__(self):
        self._employees: list[Employee] = []

    def add_employee(self, employee_data: dict):
        department_id = employee_data.get('type')  # SAL or ADM
        existing_ids = [emp.id for emp in self._employees]
        new_id = generate_unique_id(department_id, existing_ids)
        employee_data['id'] = new_id

        if self.find_employee_by_id(employee_data['id']):
            raise ValueError(f"Employee with ID {employee_data['id']} already exists.")

        employee = _create_employee_from_data(employee_data)
        self._employees.append(employee)

    def delete_employee_by_id(self, employee_id: str):
        employee = self.find_employee_by_id(employee_id)
        if not employee:
            raise ValueError(f"Employee with ID {employee_id} not found.")

        self._employees.remove(employee)

    def update_employee(self, employee_id: str, new_data: dict):
        employee_index = -1
        for i, emp in enumerate(self._employees):
            if emp.id == employee_id:
                employee_index = i
                break

        if employee_index == -1:
            raise ValueError(f"Employee with ID {employee_id} not found.")

        # Ensure the ID is not changed
        new_data['id'] = employee_id
        updated_employee = _create_employee_from_data(new_data)

        self._employees[employee_index] = updated_employee

    def get_all_employees(self) -> list[Employee]:
        return self._employees

    def find_employee_by_id(self, employee_id: str) -> Employee | None:
        for emp in self._employees:
            if emp.id == employee_id:
                return emp
        return None

    def find_employees_by_salary_range(self, min_salary: float, max_salary: float) -> list[Employee]:
        return [emp for emp in self._employees if min_salary <= emp.get_income() <= max_salary]

    def sort_employees_by_name(self) -> list[Employee]:
        return sorted(self._employees, key=lambda emp: emp.full_name)

    def sort_employees_by_income(self) -> list[Employee]:
        return sorted(self._employees, key=lambda emp: emp.get_income(), reverse=True)

    def get_top_5_employees_by_income(self) -> list[Employee]:
        return self.sort_employees_by_income()[:5]
