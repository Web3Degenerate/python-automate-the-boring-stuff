# ****************** SECOND OPTION - python's CSV module ********************************

# BETTER to use the built in csv module. Easier to parse the data later
# in particular use csv built in function reader()

import csv

with open("weather_data.csv") as data_file: 
    data = csv.reader(data_file)
    print(data)
    # This creates a CSV READER Object
    # <_csv.reader object at 0x000002126E0B7640>

    """The CSV Reader Object can be LOOPED through"""
    # for row in data:
    #     print(row)

    # This returns: 
    # <_csv.reader object at 0x000002126E0B7640>
    # ['day', 'temp', 'condition']
    # ['Monday', '12', 'Sunny']
    # ['Tuesday', '14', 'Rain']
    # ['Wednesday', '15', 'Rain']
    # ['Thursday', '14', 'Cloudy']
    # ['Friday', '21', 'Sunny']
    # ['Saturday', '22', 'Sunny']
    # ['Sunday', '24', 'Sunny']

    #each csv item is a single value

    # The temperatures is in ROW index 1
    
    temperatures = [] #empty temperatures list
    for row in data:
        if row[1] != "temp": #exclude the headers 
            #Add each temperatures aka row index 1 to our list and convert to int
            temperatures.append(int(row[1]))
    print(temperatures)

    #returns [12, 14, 15, 14, 21, 22, 24]