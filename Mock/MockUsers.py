from faker import Faker
from models.User import User
from models.Role import Role

def GenerateUsers(itemsNum):
    results = []
    
    faker = Faker()
    
    for i in range(itemsNum):
        user = GenerateUser()
        results.append(user)

    return results

def GenerateUser():
    faker = Faker()

    user = User()
    user.username = faker.profile()["username"]
    user.first_name = faker.first_name()
    user.last_name = faker.last_name()
    user.email = faker.profile()["mail"]
    user.role = Role.USER

    return user
