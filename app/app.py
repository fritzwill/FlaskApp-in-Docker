from flask import Flask, render_template
# include request above if you want request methods
# include render_template above
app = Flask(__name__)

# @app.route('/')
# def index():
# 	return "Flask Dockerized"

##### REQUEST METHODS #####
# @app.route("/")
# def index():
# 	return "Method used: %s" % request.method

# @app.route(".bacon", methods=['GET', 'POST'])
# def bacon():
# 	if request.method == 'POST':
# 		return "You are using POST"
# 	else:
# 		return "You are probably using GET"

##### HTML TEMPLATES #####
# @app.route("/profile/<name>")
# def profile(name):
# 	return render_template("profile.html", name=name)

##### PASSSING OBJECTS #####
@app.route("/shopping")
def shpping():
	food = ["Cheese", "Tuna", "Beef"]
	return render_template("shopping.html", food=food)
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)