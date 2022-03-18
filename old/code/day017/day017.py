class User:
    #pass #for when you want to skip
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1 #you're passing a username to follow
        self.following += 1 #this is the follower account of the instanciated object, itself



user_1 = User("001", "chris")
user_2 = User("002", "jill")
# user_1.id = "001"
# user_1.username = "chris"

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
