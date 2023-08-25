import random


def generate_employee_details(num_employees):
    emp_locations = [
        "Kormangala", "HSR Layout", "Ballary", "Mumbai",
        "Chennai", "Nellore", "Gurgaon", "Hyderabad"
    ]

    for i in range(num_employees):
        emp_id = random.randint(1, 9999)
        emp_location = random.choice(emp_locations)
        emp_salary = random.randint(20000, 150000)

        yield {
            "Emp Id": emp_id,
            "Emp Location": emp_location,
            "Emp Salary": emp_salary
        }


def employees():
    try:
        num_employees = int(input("Enter the number of employee details to generate: "))
        employee_generator = generate_employee_details(num_employees)

        for employee in employee_generator:
            print("Employee Details:")
            print("Emp Id:", employee["Emp Id"])
            print("Emp Location:", employee["Emp Location"])
            print("Emp Salary:", employee["Emp Salary"])
            print()

    except ValueError:
        print("Please enter a valid number.")

employees()