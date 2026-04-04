import os

def generate_invitations(template, attendees):
	if not isinstance(template, str):
		print("Error: Template must be a string")
		return None
	# if template == None or template == "" This code is abbreviated as follows:
	if not template:
		print("Template is empty, no output files generated.")
		return
	if not isinstance(attendees, list):
		print("Error: Attendees must be a list")
		return
	if not attendees:
		print("No data provided, no output files generated.")
		return
	if not all(isinstance(x, dict) for x in attendees):
		print("Error: Attendees must be a list of dictionaries")
		return

	for index , attendee in enumerate(attendees, start=1):
		invitation_text = template

		name = attendee.get('name', 'N/A')	
		if name is None:
			name = 'N/A'
		invitation_text = invitation_text.replace('{name}', name)

		title = attendee.get('event_title', 'N/A')
		if title is None:
			title = 'N/A'
		invitation_text = invitation_text.replace('{event_title}', title)

		date = attendee.get('event_date', 'N/A')
		if date is None:
			date = 'N/A'
		invitation_text = invitation_text.replace('{event_date}', date)

		location = attendee.get('event_location', 'N/A')
		if location is None:
			location = 'N/A'
		invitation_text = invitation_text.replace('{event_location}', location)

		filename = f"output_{index}.txt"
				
		try:
			if os.path.exists(filename):
				print(f"Warning: {filename} already exists, overwriting...")

			with open(filename, 'w', encoding='utf-8') as file:
				file.write(invitation_text)

			print(f"Generated: {filename}")
		except Exception as e:
		    print(f"Error writing {filename}: {e}")
