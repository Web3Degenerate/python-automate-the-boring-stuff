# Modifying Global Scope

enemies = 2



""" ******************* PASSING IT IN AS A PARAMETER & Return Statement ********************************"""

def increase_enemies_return(enemy):
    print(f"enemies inside increase_enemies_return function: {enemies}")
    return enemy + 1


enemies = increase_enemies_return(enemies)
print(f"enemies outside increase_enemies_return function: {enemies}")





""" ******************* USING THE GLOBAL KEYWORD SOLUTION ********************************"""

def increase_enemies():
    global enemies # USE GLOBAL KEYBOARD to change our global variable `enemies`
    # enemies = 37

    print(f"enemies inside function: {enemies}")
    enemies += 2


# increase_enemies() # won't work with our print statement. set it to global variable
increase_enemies()
print(f"enemies outside function: {enemies}")


