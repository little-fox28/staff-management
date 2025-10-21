from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.employee.employee import Employee


class IEmployeeService(ABC):
    """
    Interface for a service that manages employee data.
    """

    @abstractmethod
    def add_employee(self, employee_data: Dict) -> None:
        """Adds a new employee."""
        pass

    @abstractmethod
    def delete_employee_by_id(self, employee_id: str) -> None:
        """Deletes an employee by their ID."""
        pass

    @abstractmethod
    def update_employee(self, employee_id: str, new_data: Dict) -> None:
        """Updates an employee's information."""
        pass

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        """Returns a list of all employees."""
        pass

    @abstractmethod
    def find_employee_by_id(self, employee_id: str) -> Optional[Employee]:
        """Finds an employee by their ID."""
        pass

    @abstractmethod
    def find_employees_by_salary_range(self, min_salary: float, max_salary: float) -> List[Employee]:
        """Finds employees within a given salary range."""
        pass

    @abstractmethod
    def sort_employees_by_name(self) -> List[Employee]:
        """Sorts employees by name."""
        pass

    @abstractmethod
    def sort_employees_by_income(self) -> List[Employee]:
        """Sorts employees by income."""
        pass

    @abstractmethod
    def get_top_5_employees_by_income(self) -> List[Employee]:
        """Gets the top 5 employees by income."""
        pass
