import pandas
data = pandas.read_csv("squirrel_count_raw.csv")

# Get a hold of the column we want in our DataFrame
grey_squirrels = data["Primary Fur Color"] == "Gray"
# print(grey_squirrels) #3022 columns, it just shows you the first few .. and last few


# ======================== Get three Squirrel Type Count ================
# Gray squirrel Count
grey_squirrels_count = len(data["Primary Fur Color"] == "Gray")
# print(grey_squirrels_count) #returns 3023

# Cinnamon squirrel Count
red_squirrels_count = len(data["Primary Fur Color"] == "Cinnamon")

# Cinnamon squirrel Count
black_squirrels_count = len(data["Primary Fur Color"] == "Black")


#===== Construct DataFrame with our three squirrel values, Gray, Red and Black ===

# dictionary with two key value pairs
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# Initialize our dictionary with pandas.DataFrame()
df = pandas.DataFrame(data_dict)

# Convert our df to csv and save to local directory as squirrel_count.csv
df.to_csv("squirrel_count.csv")

