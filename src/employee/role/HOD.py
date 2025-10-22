from ..employee import Employee

class HOD:
    """Decorator to add HOD responsibilities to an employee."""

    def __init__(self, employee: Employee, responsibility_salary: float = 0.0):
        self._employee = employee
        self._responsibility_salary = responsibility_salary
        self._employee.role = "HOD"

    @property
    def role(self):
        return self._employee.role

    @property
    def responsibility_salary(self) -> float:
        return self._responsibility_salary

    @responsibility_salary.setter
    def responsibility_salary(self, value: float):
        if value < 0:
            raise ValueError("Lương trách nhiệm phải là số không âm.")
        self._responsibility_salary = value

    def get_income(self) -> float:
        """Income = base income + responsibility salary."""
        return self._employee.get_income() + self.responsibility_salary

    def calc_tax(self) -> float:
        """Calculate income tax based on income brackets."""
        taxable_income = self.get_income()
        if taxable_income is None or taxable_income < 0:
            raise ValueError("Thu nhập phải là một số không âm.")

        if taxable_income < 9_000_000:
            return 0.0
        elif taxable_income <= 15_000_000:
            return taxable_income * 0.10
        else:
            return taxable_income * 0.12

    def __getattr__(self, name):
        """Delegate other attribute access to the wrapped employee."""
        return getattr(self._employee, name)

    def __str__(self):
        return (
            f"Mã: {self.id} | Họ tên: {self.full_name} | "
            f"Lương cơ bản: {self.basic_salary:,.0f} | "
            f"Thu nhập: {self.get_income():,.0f} | "
            f"Thuế: {self.calc_tax():,.0f} | "
            f"Vai trò: {self.role} | "
            f"Lương trách nhiệm: {self.responsibility_salary:,.0f}"
        )