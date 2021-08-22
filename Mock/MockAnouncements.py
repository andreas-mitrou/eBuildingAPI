from faker import Faker
from models.Announcement import Announcement
from random import randrange

def GenerateAnouncements(itemsNum):
    results = []
    
    faker = Faker()
    
    for i in range(itemsNum):
        announcement = GenerateAnouncement()
        results.append(announcement)

    return results

def GenerateAnouncement():
    faker = Faker()
    rndInt = randrange(1,100)
    anouncement = Announcement(**{"id":rndInt, "header":"Title: " + str(rndInt),"content":faker.text()})
    return anouncement