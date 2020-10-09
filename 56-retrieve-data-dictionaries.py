emails = {
    'caleb':'caleb@gmail.com',
    'gal':'g@hotmail.com',
    'tim':'timmy@sapo.pt',
}
if 'caleb' in emails:
    print(emails['caleb'])
else:
    print('not found')

print(emails.get('caleb'))
#if it doesn't exist returns 'none'
print(emails.get('joao','no user found'))
#this last one with personalized message