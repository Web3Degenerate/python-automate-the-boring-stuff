game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) #prints Skeleton


def create_enemy():
    #Function LOCAL SCOPE: only available in create_enemy() function
    if game_level < 5:
        newer_enemy = enemies[0]

    #can only print newer_enemy within function
    print(newer_enemy)

print(newer_enemy) #out of scope now that our if stmt is in a function

create_enemy() #prints Skeleton


#********************************************

game_level_error = 10
enemies_error = ["Skeleton", "Zombie", "Alien"]

def create_enemy_error():
    # To resolve UNDEFINED error if our IF condition is not met, define it above the conditional
    newer_enemy = "Sorry, your game level is not high enough."
    if game_level_error < 5:
        newer_enemy = enemies_error[0]

    print(newer_enemy)

create_enemy_error() #prints Skeleton