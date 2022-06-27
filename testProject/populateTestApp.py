import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','testProject.settings')

import django
django.setup()

import random
from testApp.models import Users
from faker import Faker

fakeGen = Faker()

def populate(N=5):


    for entry in range(N):
            fakename = fakeGen.name().split()
            fakeLastName = fakename[0]
            fakeFirstName = fakename[1]
            fakeEmail = fakeGen.email()

            users = Users.objects.get_or_create(firstName = fakeFirstName,lastName = fakeLastName,email = fakeEmail)[0]

if __name__ == '__main__':
    print("Populating")
    populate(10)
    print("Populating Complete")
