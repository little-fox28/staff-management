from ..employee import Employee

class AdminStaff(Employee):
    """Administrative staff class."""
    def __init__(self, emp_id: str, full_name: str, basic_salary: float):
        super().__init__(emp_id, full_name, basic_salary)
        self.department_id = "ADM"

    def get_income(self) -> float:
        """Income = base salary."""
        return self.basic_salary
