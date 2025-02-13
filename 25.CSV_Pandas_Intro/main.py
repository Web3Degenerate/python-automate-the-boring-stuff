import pandas

data = pandas.read_csv("weather_data.csv")
    # don't have to open the file as a data file
    # one step and your done

print(data) #prints out table much better
print(type(data)) # DataFrame returns <class `pandas.core.frame.DataFrame`>


print(data["temp"]) #prints out just the temp column
print(type(data["temp"])) # Series returns <class `pandas.core.series.Series`>


# Turn DataFrame into a Dictionary with Method to_dict()
data_dict = data.to_dict()
print(data_dict)

# Turn Series into a List with Method to_list()
temp_list = data["temp"].to_list()
print(temp_list)
# Then you can do all the things you can with a list, like return the length - len()
print(f"The size of this list series is {len(temp_list)}")

# Average: https://www.geeksforgeeks.org/find-average-list-python/
avg = sum(temp_list) / len(temp_list)
print(f"The average of this list series is {avg}")

# Average with Pandas' built-in method .mean()
panda_avg = data["temp"].mean()
# print(f'Mean with Panda .mean() method is: {panda_avg}')
print(f'Mean with Panda .mean() method is: {data["temp"].mean()}')


# Get the max Temperature value
# max_value = data["temp"].max()
max_value = data.temp.max()
print(max_value) #returns 24

# TWO was to call csv headers
# 1. data["temp"]
# 2. data.temp


#**** GET DATA IN A ROW in our csv data *****

"""weather_data.csv

day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
...
Sunday,24,Sunny
"""

#To select the Monday Row: 
data[data.day == "Monday"]
# print(f'Here is the Monday Row: {data[data.day == "Monday"]}')
print(data[data.day == "Monday"])

# Pull out whichever row had the max temperature (here Sunday)
# LOGIC: data.temp == data.temp.max()
# place into the data[]
data[data.temp == data.temp.max()]
print(data[data.temp == data.temp.max()]) #6 Sunday 24 Sunny

# Pull up a specific Row - Monday (day column)
# get the CONDITION column for just Monday's row
monday = data[data.day == "Monday"]
print(f"Monday's Condition column was {monday.condition}")

# Convert Monday's Celsius Temperature to Fahrenheit
monday_fahrenheit = monday.temp[0] * 9/5 + 32 #================> returns 53.6
print(f"Monday's temp in F was {monday_fahrenheit}")


print(f"Monday.temp is \n {monday.temp}") #returns 0  12
                                        #        Name: temp, dtpye: int64 
print(f"Monday.temp[0] is \n {monday.temp[0]}") #returns 12



########### CREATE DATA FRAME FROM SCRATCH ###################################

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}


# Call our pandas library and then our DataFrame Class
new_df = pandas.DataFrame(data_dict) # initalize that df class with our data_dict data
print(new_df)


## NOW WE CAN CONVERT OUR new_df DataFrame to csv with the .to_csv() method
# Just needs the required param of the path you want to save csv file to.

# SAME directory, just give it a name
new_df.to_csv("new_df.csv")