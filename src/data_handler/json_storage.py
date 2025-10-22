import json
from src.data_handler.IStorage import IStorage
from src.employee.employee import Employee
from src.employee.role.adminstrative import AdminStaff
from src.employee.role.sales import SalesStaff
from src.employee.role.HOD import HOD


class JSONStorage(IStorage):
    def _to_dict(self, employee: Employee) -> dict:
        data = {
            'id': employee.id,
            'full_name': employee.full_name,
            'basic_salary': employee.basic_salary,
            'department_id': employee.department_id,
            'role': employee.role,
        }
        if isinstance(employee, HOD):
            data['responsibility_salary'] = employee.responsibility_salary
            employee = employee._employee  # Get the wrapped employee

        if isinstance(employee, SalesStaff):
            data['type'] = 'SAL'
            data['sales_amount'] = employee.sales_amount
            data['commission_rate'] = employee.commission_rate
        elif isinstance(employee, AdminStaff):
            data['type'] = 'ADM'
        else:
            data['type'] = 'Employee' # Should not happen with current structure
        return data

    def _from_dict(self, data: dict) -> Employee:
        emp_type = data.get('type')
        employee = None

        if emp_type == 'SAL':
            employee = SalesStaff(
                emp_id=data['id'],
                full_name=data['full_name'],
                basic_salary=data['basic_salary'],
                sales_amount=data.get('sales_amount', 0.0),
                commission_rate=data.get('commission_rate', 0.0)
            )
        elif emp_type == 'ADM':
            employee = AdminStaff(
                emp_id=data['id'],
                full_name=data['full_name'],
                basic_salary=data['basic_salary']
            )

        if not employee:
            raise ValueError(f"Unknown employee type: {emp_type}")

        if data.get('role') == 'HOD':
            employee = HOD(employee, responsibility_salary=data.get('responsibility_salary', 0.0))

        return employee

    def save(self, file_path: str, employees: list[Employee]):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([self._to_dict(emp) for emp in employees], f, indent=4, ensure_ascii=False)

    def load(self, file_path: str) -> list[Employee]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [self._from_dict(emp_data) for emp_data in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
