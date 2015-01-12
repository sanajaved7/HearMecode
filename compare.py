employees_dict = {}
survey_people = {}

with open("survey.csv", "r") as survey_file:
	survey = survey_file.read().split("\n")
for x in survey:
	s_email, s_twitter, s_github = x.split(",")
	survey_people[s_email] = {'twitter': s_twitter, 'github': s_github} 

with open("all_employees.csv", "r") as employees_file: 
	employees = employees_file.read().split("\n")
for y in employees:
	e_name, e_email, e_phone, e_department, e_position = y.split(",")
	e_email = e_email.strip()
	employees_dict[e_name] = {'email': e_email, 'phone': e_phone, 'department': e_department, 'position': e_position}
	if survey_people.get(e_email):
		print e_name + " took the survey! Here is their information:\n\nPhone:" + e_phone + "\n\nDepartment:" + e_department + "\n\nPosition:" + e_position + "\n\nTwitter:" + survey_people.get(e_email).get('twitter') + "\n\nGithub:" + survey_people.get(e_email).get('github') + '\n\n\n'
