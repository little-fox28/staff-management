from ..employee import Employee

class HOD:
    """Decorator to add HOD responsibilities to an employee."""

    def __init__(self, employee: Employee, responsibility_salary: float = 0.0):
        self._employee = employee
        self._responsibility_salary = responsibility_salary
        self._employee.role = "HOD"

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

    def __getattr__(self, name):
        """Delegate other attribute access to the wrapped employee."""
        return getattr(self._employee, name)