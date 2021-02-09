from flask import Flask, flash, jsonify, redirect, render_template, request
from script import get_data_and_save_to_db
from get_db_script import get_db

# Configure application
app = Flask(__name__)
app.config['DEBUG'] = True

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
	if request.method != 'POST':
		get_db("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, user_id TEXT, gender TEXT NOT NULL, name TEXT NOT NULL, loc_strt TEXT NOT NULL, loc_ccsp TEXT NOT NULL, loc_cord TEXT NOT NULL, loc_tmz TEXT NOT NULL, email TEXT NOT NULL UNIQUE, log_uuid TEXT NOT NULL, log_username TEXT NOT NULL, log_password TEXT NOT NULL, log_salt TEXT NOT NULL, log_md5 TEXT NOT NULL, log_sha1 TEXT NOT NULL, log_sha256 TEXT NOT NULL, dob TEXT NOT NULL, registered TEXT NOT NULL, phone TEXT NOT NULL, cell TEXT NOT NULL, user_id_name TEXT NOT NULL, picture_thumb TEXT NOT NULL, nat TEXT NOT NULL)")
		users = get_db("SELECT * FROM users;")
		if users == None:
			return render_template("index.html")
		else:
			return render_template("index.html", users=users)
	if request.method == 'POST':
		user = get_db("SELECT * FROM users WHERE email = %s", (request.form.get("search"),))
		if user != []:
			return render_template("index.html", user=user)
		if user == []:
			return render_template("index.html", error="User not found")
	
@app.route("/create_users", methods=["GET", "POST"])
def create_users():
	if request.method == 'POST':
		get_data_and_save_to_db()
		return redirect("/")
		
@app.route("/delete_users", methods=["GET", "POST"])
def delete_users():
	if request.method == 'POST':
		get_db("DELETE FROM users")
		return redirect("/")
		
@app.route("/delete_user", methods=["GET", "POST"])
def delete_user():
	if request.method == 'POST':
		get_db("DELETE FROM users WHERE name = %s",  (request.form.get("name"),))
		return redirect("/")
		
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
	

