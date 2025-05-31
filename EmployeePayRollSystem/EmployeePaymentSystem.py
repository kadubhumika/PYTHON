# Employee Payment System
# Base class
class Employee:
    company = "Google"

    def __init__(self, name, base_salary, debtamount, work, work_experience):
        self.name = name
        self.salary = base_salary
        self.debt = debtamount
        self.work = work
        self.work_experience = work_experience

    def calculate_salary(self):
        return self.salary + self.debt + self.work_experience

    def __repr__(self):
        return (f"{self.__class__.__name__} {self.name} | Role: {self.work} | "
                f"Experience: {self.work_experience} years | "
                f"Total Salary: ₹{self.calculate_salary()} | Company: {self.company}")


# Subclasses with different salary logic (example modifiers)
class FullEmployee(Employee):
    def calculate_salary(self):
        return self.salary + self.debt + self.work_experience * 1000


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return (self.salary * 0.6) + self.debt + self.work_experience * 500


class InternEmployee(Employee):
    def calculate_salary(self):
        return (self.salary * 0.3) + self.debt + self.work_experience * 200


# Function to create employee with user input
def create_employee():
    name = input("Enter Employee name: ")
    base_salary = float(input("Enter base salary: "))
    debtamount = float(input("Enter debt amount: "))
    work = input("Enter role/work: ")
    work_experience = int(input("Enter years of experience: "))
    emp_type = input("Enter employee type (full/part/intern): ").strip().lower()

    if emp_type == "full":
        return FullEmployee(name, base_salary, debtamount, work, work_experience)
    elif emp_type == "part":
        return PartTimeEmployee(name, base_salary, debtamount, work, work_experience)
    elif emp_type == "intern":
        return InternEmployee(name, base_salary, debtamount, work, work_experience)
    else:
        print("Invalid employee type!")
        return None


# Main logic
employees = []

n = int(input("How many employees do you want to add? "))
for _ in range(n):
    emp = create_employee()
    if emp:
        employees.append(emp)

# Output
print("\nEmployee Payroll Report:")
for emp in employees:
    print(emp)
