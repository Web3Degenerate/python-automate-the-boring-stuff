class User:
    """To create an empty class, use the pass keyword"""
    # pass

    # def __init__(self) -> None:
    #     pass

    def __init__(self, user_id, user_name):
        # set up user id place holder
        self.id = user_id
        self.user_name = user_name
        # We can set up default values, like followers = 0
        self.followers = 0
        

# Classes use PascalCase
# as distinguished from 
#camelCase
#snake_case


#v.118 Adding attributes to an object
# user_1 = User()
# user_1.id = "001"
# user_1.username = "steve"
# print(user_1.username)

user_1 = User("69", "Alba")
print(user_1.user_name)
user_1.followers = 69
print(f'{user_1.user_name} has {user_1.followers} followers')

# Constructor - what happen when object is created, hence when it is initialized. 
# use the init function
# in python: 
##  def __init__(self)

# resume at v119 - Adding Methods to a Class.