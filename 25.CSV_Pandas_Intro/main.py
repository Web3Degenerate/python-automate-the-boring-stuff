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