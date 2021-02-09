import requests
from get_db_script import get_db

def get_data_and_save_to_db():
	response = requests.get(f"https://randomuser.me/api/?results=100&gender=male")
	response_json = response.json()
	
	for dictionary in response_json['results']:
		gender = dictionary['gender']
		name = dictionary['name']['title'] + " " + dictionary['name']['first'] + " " + dictionary['name']['last']
		location_street = str(dictionary['location']['street']['number']) + ", " + dictionary['location']['street']['name']
		location_ccsp = dictionary['location']['city'] + ", " + dictionary['location']['state'] + ", " + dictionary['location']['country'] + ", " + str(dictionary['location']['postcode'])
		location_cord = dictionary['location']['coordinates']['latitude'] + ", " + dictionary['location']['coordinates']['longitude']
		location_timezone = dictionary['location']['timezone']['offset'] + ", " + dictionary['location']['timezone']['description']
		email = dictionary['email']
		uuid = dictionary['login']['uuid']
		username = dictionary['login']['username']
		password = dictionary['login']['password']
		salt = dictionary['login']['salt']
		md5 = dictionary['login']['md5']
		sha1 = dictionary['login']['sha1']
		sha256 = dictionary['login']['sha256']
		dob = dictionary['dob']['date'] + ", " + str(dictionary['dob']['age'])
		registered = dictionary['registered']['date'] + ", " + str(dictionary['registered']['age'])
		phone = dictionary['phone']
		cell = dictionary['cell']
		user_id_name = dictionary['id']['name']
		user_id = dictionary['id']['value']
		picture = dictionary['picture']['thumbnail']
		nat = dictionary['nat']
		
		get_db("INSERT INTO users (user_id, gender, name, loc_strt, loc_ccsp, loc_cord, loc_tmz, email, log_uuid, log_username, log_password, log_salt, log_md5, log_sha1, log_sha256, dob, registered, phone, cell, user_id_name, picture_thumb, nat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
			  (user_id, gender, name, location_street, location_ccsp, location_cord, location_timezone, email, uuid, username, password, salt, md5, sha1, sha256, dob, registered, phone, cell, user_id_name, picture, nat,))
