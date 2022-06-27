import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstProject.settings')

import django
django.setup()

import random
from firstApp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakeGen = Faker()
topics = ['social','Entertainmennt','Network','news','Informative']
def addTopic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):


    for entry in range(N):

            topicgen  = addTopic()

            fakeUrl = fakeGen.url()
            fakeDate = fakeGen.date()
            fakeName = fakeGen.company()

            webpage = Webpage.objects.get_or_create(topic = topicgen,name = fakeName,url = fakeUrl)[0]

            accessDate = AccessRecord.objects.get_or_create(name = webpage,date = fakeDate)[0]

if __name__ == '__main__':
    print("Populating")
    populate(10)
    print("Populating Complete")
