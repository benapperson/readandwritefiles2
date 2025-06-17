with open("employee_data.csv", encoding="utf-8") as employeedata:
    next(employeedata)


    for line in employeedata:
        data = line.strip().split(",")
        name = data[1]
        salary = float(data[3])
        bonus_percent = float(data[7])
        bonus_amount = salary * bonus_percent
        total_pay = salary + bonus_amount

        print(f"Name: {name}")
        print(f"Salary:  ${salary:,.2f}")
        print(f"Bonus:   ${bonus_amount:,.2f}")
        print(f"Pay:     ${total_pay:,.2f}")

        input()


