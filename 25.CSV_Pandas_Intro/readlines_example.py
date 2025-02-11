# use readlines() method to create a list named data from values in weather_data.csv
# Use relative file path (same directory) to read weather_data.csv

with open("weather_data.csv") as data_file: 
    """Use readlines() not just read() to get each line as item in our list"""
    data = data_file.readlines()
    print(data)

    # Returns our list: 
    #['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 
    # 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 
    # 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

    # Not great to iterate through