with open("customers.csv") as customers, open("customer_country.csv", "w") as country:
    _ = customers.readline()
    country.write("FirstName,LastName,Country\n")
    for line in customers:
        values = line.split(",")
        country.write(values[1] + "," + values[2] + "," + values[4] + "\n")
