from src.employee.service.employee_service import EmployeeService


def _get_employee_data(emp_type: str) -> dict[str, str | float] | None:
    full_name = input("Enter full name: ")
    try:
        basic_salary = float(input("Enter basic salary: "))
    except ValueError:
        print("Invalid salary.")
        return None

    data = {
        'full_name': full_name,
        'basic_salary': basic_salary,
        'type': emp_type
    }

    if emp_type == 'SAL':
        try:
            sales_amount = float(input("Enter sales amount: "))
            commission_rate = float(input("Enter commission rate: "))
            data['sales_amount'] = sales_amount
            data['commission_rate'] = commission_rate
        except ValueError:
            print("Invalid sales or commission value.")
            return None

    is_hod = input("Is this employee a Head of Department (HOD)? (yes/no): ").lower()
    if is_hod == 'yes':
        responsibility_salary = float(input("Enter responsibility salary: "))
        data['role'] = 'HOD'
        data['responsibility_salary'] = responsibility_salary
    else:
        data['role'] = None

    return data


class MenuHandler:
    def __init__(self):
        self.employee_service = EmployeeService()

    def add_employee(self):
        print("\n--- Add New Employee ---")
        emp_type = input("Enter employee type (ADM for Admin, SAL for Sales): ").upper()
        if emp_type not in ['ADM', 'SAL']:
            print("Invalid employee type.")
            return
        
        employee_data = _get_employee_data(emp_type)
        if employee_data:
            try:
                self.employee_service.add_employee(employee_data)
                print("Employee added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

    def show_all_employees(self):
        print("\n--- List of Employees ---")
        employees = self.employee_service.get_all_employees()
        if not employees:
            print("No employees found.")
        else:
            for emp in employees:
                print(emp)

    def find_employee_by_id(self):
        print("\n--- Find Employee by ID ---")
        emp_id = input("Enter employee ID to find: ")
        employee = self.employee_service.find_employee_by_id(emp_id)
        if employee:
            print(f"Found employee: {employee}")
        else:
            print(f"No employee found with ID '{emp_id}'.")

    def delete_employee_by_id(self):
        print("\n--- Delete Employee by ID ---")
        emp_id = input("Enter employee ID to delete: ")
        try:
            self.employee_service.delete_employee_by_id(emp_id)
            print(f"Employee with ID '{emp_id}' has been deleted.")
        except ValueError as e:
            print(f"Error: {e}")

    def update_employee(self):
        print("\n--- Update Employee Information ---")
        emp_id = input("Enter employee ID to update: ")
        employee = self.employee_service.find_employee_by_id(emp_id)
        if not employee:
            print(f"No employee found with ID '{emp_id}'.")
            return

        print("Enter new information for the employee:")
        new_data = _get_employee_data(employee.department_id)
        if new_data:
            try:
                self.employee_service.update_employee(emp_id, new_data)
                print(f"Employee '{emp_id}' has been updated.")
            except ValueError as e:
                print(f"Error: {e}")

    def find_employees_by_salary(self):
        print("\n--- Find Employees by Salary Range ---")
        try:
            min_salary = float(input("Enter minimum salary: "))
            max_salary = float(input("Enter maximum salary: "))
            if min_salary > max_salary:
                print("Minimum salary cannot be greater than maximum salary.")
                return
            employees = self.employee_service.find_employees_by_salary_range(min_salary, max_salary)
            if not employees:
                print("No employees found in this salary range.")
            else:
                for emp in employees:
                    print(emp)
        except ValueError:
            print("Salary must be a number.")

    def sort_employees_by_name(self):
        print("\n--- Employees Sorted by Name ---")
        sorted_employees = self.employee_service.sort_employees_by_name()
        for emp in sorted_employees:
            print(emp)

    def sort_employees_by_income(self):
        print("\n--- Employees Sorted by Income ---")
        sorted_employees = self.employee_service.sort_employees_by_income()
        for emp in sorted_employees:
            print(emp)

    def show_top_5_by_income(self):
        print("\n--- Top 5 Employees by Income ---")
        top_employees = self.employee_service.get_top_5_employees_by_income()
        if not top_employees:
            print("No employees to show.")
        else:
            for emp in top_employees:
                print(emp)