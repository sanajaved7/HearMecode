contacts = {
	'Sana Javed': {'phone': '123456789', 'twitter': '@sanajaved', 'github': '@sanajaved7'},

	'Risa Ohara': {'phone': '123456789', 'twitter': '@riohimo', 'github': 'rioh'}, 

	'Sarah-Jaine Szekeresh': {'phone': '123456789', 'github': 'SarahJaine', 'twitter': 'none'}
}

for contact in contacts:
	print contact + "'s contact information is:\nPhone: " + contacts.get(contact).get('phone') + "\nTwitter:" + contacts.get(contact).get('twitter') + "\nGithub:" + contacts.get(contact).get('github') + "\n"