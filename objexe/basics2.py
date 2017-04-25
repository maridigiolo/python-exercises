class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))

#5,6
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))

    def add_friends(self, other):
        friends = []
        self.friends.append(other)

    def num_friends(self):
        qt = len(self.friends)
        print(qt)

    def greeting_count(self):
        count = 0
        if self.greet() == True:
            count += 1
            print (count)


#1
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948',[])
#2
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])


#3
sonny.greet('Jordan')
sonny.greeting_count()
#4
jordan.greet('Sonny')


#Ex 2 - ownclass - add method 2
sonny.print_contact_info()
# #5
# print('Sonny information is: ' + sonny.email, sonny.phone)


#Ex 2 - ownclass - add method 2
jordan.print_contact_info()
# #6
# print('Jordan information is: ' + jordan.email, jordan.phone)


#Ex2 - ownclass - adding a instance variable (attribute)
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print(len(jordan.friends))
# print(len(sonny.friends))

#Ex2 - ownclass - add a add_friend method
jordan.add_friends(sonny)
sonny.add_friends(jordan)

#Ex2 - ownclass - add a num_friend method
jordan.num_friends()
sonny.num_friends()
