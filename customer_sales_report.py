salessum = dict()

with open("sales.csv") as sales:
    _ = sales.readline()

    for line in sales:
        values = line.split(",")
        # print(values)
        total = float(values[3]) + float(values[4]) + float(values[5])
        # print("CustID %s total %.2f" % (values[0], total))

        if values[0] in salessum:
            salessum[values[0]] += total
        else:
            salessum[values[0]] = total

with open("salesreport.csv", "w") as salesreport:
    salesreport.write("CustomerID,Total\n")
    for custID, sumvalue in salessum.items():
        salesreport.write("%s,%.2f\n" % (custID, sumvalue))

