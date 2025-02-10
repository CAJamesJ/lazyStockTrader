import csv 

list_of_csv = list()
  
with open('VOO_close_25_01.csv', 'r') as read_obj: 
    # Return a reader object which will
    # iterate over lines in the given csvfile
    csv_reader = csv.reader(read_obj)

    result = []

    for day in csv_reader:
        result.append(day[1])

    # convert string to list
    list_of_csv = list(result)

    # print(list_of_csv)

cost = 0
totalShares = 0

for i in range(3, len(list_of_csv)): #csv have 3 initial rows that are not valid
    try:
        cost += float(list_of_csv[i]) 
        totalShares += 1
    except ValueError:
        print(f"Skipping invalid price: {i, list_of_csv[i]}")

# print(cost, totalShares)
# print(totalShares*float(list_of_csv[-1])/cost)
print(f"The cost was {cost} and it could be {totalShares*float(list_of_csv[-1])}")

# print(totalShares*int(list_of_csv[-1])/cost)

    