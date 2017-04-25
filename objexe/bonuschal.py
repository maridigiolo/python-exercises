class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greet_count = 0
        self.num_unique_people_greeted = 0
        self.uniquetracker = []


    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
        # print ('Person: {} {} {}'.format(self.name, self.email, self.phone))


    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))
        self.greet_count += 1
        if other_person not in self.uniquetracker:
            self.uniquetracker.append(other_person)
            self.num_unique_people_greeted += 1

#5,6
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))

    def add_friends(self, other):
        friends = []
        self.friends.append(other)

    def num_friends(self):
        qt = len(self.friends)
        print(qt)


#1
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948',[])
#2
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])


#3
sonny.greet('Jordan')
sonny.greet('Jordan')
sonny.greet('Lili')
sonny.greet('Mary')
sonny.greet('Joe')



#4
# jordan.greet('Sonny')


#Ex 2 - ownclass - add method 2
# sonny.print_contact_info()
# #5
# print('Sonny information is: ' + sonny.email, sonny.phone)


#Ex 2 - ownclass - add method 2
# jordan.print_contact_info()
# #6
# print('Jordan information is: ' + jordan.email, jordan.phone)


#Ex2 - ownclass - adding a instance variable (attribute)
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print(len(jordan.friends))
# print(len(sonny.friends))

#Ex2 - ownclass - add a add_friend method
# jordan.add_friends(sonny)
# sonny.add_friends(jordan)

#Ex2 - ownclass - add a num_friend method
# jordan.num_friends()
# sonny.num_friends()

# print(sonny.greet_count)
# print(jordan.greet_count)

# print(jordan.num_unique_people_greeted)
print(sonny.num_unique_people_greeted)


# print(jordan)
#If you want a print in other way, you can use this:
# jordan.__str__()
#but, remeber, to use that you should print instead of return when you def you str function.

# print(sonny)
# sonny.__str__()
