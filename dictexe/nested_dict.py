#!/usr/bin/env python3

info = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
# step 1- print Ramit's address email
print (info['email'])
# step 2- get the first of Ramit's interests
print (info['interests'][0])
# step 3- get the email address of jasmine
print (info['friends'][0]['email'])
# step 4- get the second of Jan's two interests
print (info['friends'][1]['interests'][1])
