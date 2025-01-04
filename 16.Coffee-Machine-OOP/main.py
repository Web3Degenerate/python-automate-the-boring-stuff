# import prettytable

# See PrettyTable Reference: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

#sec 16, video 112

from prettytable import PrettyTable
table = PrettyTable() 
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)