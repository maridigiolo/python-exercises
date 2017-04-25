# Given the following Person class:
#
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def greet(self, other_person):
#         print 'Hello {}, I am {}!'.format(other_person.name, self.name)
# Write code to
#
# 1 - Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# 2 - Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# 3 - Have sonny greet jordan using the greet method.
# 4 - Have jordan greet sonny using the greet method.
# 5 - Write a print statement to print the contact info (email and phone) of Sonny.
# 6 - Write another print statement to print the contact info of Jordan.

class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person, self.name))

#5,6
    # def print_contact_info(self):
    #     print("{}'s email: {}, {}'s phone number: {}".format(self.name, self.email, self.name, self.phone))
    #

#1
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948',[])
#2
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])


#3
sonny.greet('Jordan')
#4
jordan.greet('Sonny')


#Ex 2 - ownclass - add method 2
#sonny.print_contact_info()
#5
print('Sonny information is: ' + sonny.email, sonny.phone)


#Ex 2 - ownclass - add method 2
#jordan.print_contact_info()
#6
print('Jordan information is: ' + jordan.email, jordan.phone)
