class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"{self.id}, {self.username} created")

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    def printFollowers(self):
        print(f"{self.username}'s followers: {self.followers}")


first_user = User("0", "greenMakaroni")
second_user = User("15", "someOtherGuy")

first_user.printFollowers()
second_user.printFollowers()

first_user.follow(second_user)

first_user.printFollowers()
second_user.printFollowers()
