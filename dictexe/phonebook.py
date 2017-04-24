#!/usr/bin/env python3

phonebook_dict = {
'Alice': '703-493-1834',
'Bob': '857-384-1234',
'Elizabeth': '484-584-2923'
}

#step 1 - getting a number
print(phonebook_dict.get('Elizabeth'))
#step 2 - add a name to dictionary
phonebook_dict ['Kareem']= ['938-489-1234']
#step 3 - deleting a name from the dictionary
del phonebook_dict['Alice']
# step 4 - changing numbers
phonebook_dict['Bob'] = ['968-345-2345']


print(phonebook_dict)
