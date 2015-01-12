# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

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
