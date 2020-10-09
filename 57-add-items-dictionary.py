emails = {
    'caleb':'caleb@gmail.com',
    'gal':'g@hotmail.com',
    'tim':'timmy@sapo.pt',
}

#three diferent ways

#1st way
emails['joao'] = 'joao@gmail.com'

print(emails)

#2nd way
emails.update({'joao2':'joao2@gmail.com', 'jules':'love@gmail.com'})
#3rd way
emails.update(scotishgirl = 'beautiful@gmail.com')

print(emails)