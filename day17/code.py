"""
snake_case --> everything else
PascalCase --> class name
camelCase
"""
class User:
    def __init__(self,user_id,username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    
    def follow(self,user):
        user.followers +=1
        self.following +=1
        
user_1 = User('001','aakash')
user_2 = User('002','jack')
user_1.follow(user_2)
print(user_1.followers,user_1.following)
print(user_2.id,user_2.username,user_2.follower,user_2.following)
