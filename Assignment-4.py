# Write Your Python Code here....
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employee_data(data, sorting_parameter):
    if sorting_parameter == 1:
        return sorted(data, key=lambda x: x.age)
    elif sorting_parameter == 2:
        return sorted(data, key=lambda x: x.name)
    elif sorting_parameter == 3:
        return sorted(data, key=lambda x: x.salary)
    else:
        return data


def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    while True:
        print("Sorting Options:")
        print("1. Sort by Age")
        print("2. Sort by Name")
        print("3. Sort by Salary")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        sorted_employees = sort_employee_data(employees, choice)

        print("\nSorted Employee Data:")
        for emp in sorted_employees:
            print(emp)

if __name__ == "__main__":
    main()

#......