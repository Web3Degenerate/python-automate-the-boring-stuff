
# use readlines() method to create a list named data from values in weather_data.csv
# Use relative file path (same directory) to read weather_data.csv

# with open("weather_data.csv") as data_file: 
#     """Use readlines() not just read() to get each line as item in our list"""
#     data = data_file.readlines()
#     print(data)

    # Returns our list: 
    #['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 
    # 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 
    # 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


# # ****************** SECOND OPTION - python's CSV module ********************************

# # BETTER to use the built in csv module. Easier to parse the data later
# # in particular use csv built in function reader()

# import csv

# with open("weather_data.csv") as data_file: 
#     data = csv.reader(data_file)
#     print(data)
#     # This creates a CSV READER Object
#     # <_csv.reader object at 0x000002126E0B7640>

#     """The CSV Reader Object can be LOOPED through"""
#     # for row in data:
#     #     print(row)

#     # This returns: 
#     # <_csv.reader object at 0x000002126E0B7640>
#     # ['day', 'temp', 'condition']
#     # ['Monday', '12', 'Sunny']
#     # ['Tuesday', '14', 'Rain']
#     # ['Wednesday', '15', 'Rain']
#     # ['Thursday', '14', 'Cloudy']
#     # ['Friday', '21', 'Sunny']
#     # ['Saturday', '22', 'Sunny']
#     # ['Sunday', '24', 'Sunny']

#     #each csv item is a single value

#     # The temperatures is in ROW index 1

#     temperatures = [] #empty temperatures list
#     for row in data:
#         if row[1] != "temp": #exclude the headers 
#             #Add each temperatures aka row index 1 to our list and convert to int
#             temperatures.append(int(row[1]))
#     print(temperatures)

#     #returns [12, 14, 15, 14, 21, 22, 24]

# ******************** THIRD OPTION - USING PANDAS ******************************

import pandas

data = pandas.read_csv("weather_data.csv")
    # don't have to open the file as a data file
    # one step and your done

print(data) #prints out much better

