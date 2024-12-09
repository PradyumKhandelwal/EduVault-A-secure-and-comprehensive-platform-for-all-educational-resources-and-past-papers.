from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return render_template("home.html")
        return "Invalid username or password."

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Open the CSV file and append the new user data
        with open('users.csv', 'a') as file:
            # file.write("/n")
            writer = csv.writer(file)
            writer.writerow([username, password])
        return render_template('home.html')
    else:
        return render_template('register.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/base2')
def base2():
    return render_template('base2.html')

@app.route('/eight')
def eight():
    return render_template('eight.html')
@app.route('/nine')
def nine():
    return render_template('nine.html')
@app.route('/tenth')
def tenth():
    return render_template('ten.html')
@app.route('/eleventh')
def eleventh():
    return render_template('eleven.html')
@app.route('/twelfth')
def twelfth():
    return render_template('twelve.html')

if __name__ == '__main__':
    app.run(debug=True)
