from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Replace the configuration with your actual MySQL database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Omm%40ir510219900@127.0.0.1/cloud_assignment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Home Page
@app.route('/')
def home():
    return 'Welcome to the Home Page'

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return 'Signup Successful!'

    return render_template('signup.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            return 'Login Successful!'
        else:
            return 'Login Failed. Please check your username and password.'

    return render_template('login.html')
@app.route('/view_users')
def view_users():
    users = User.query.all()
    return render_template('view_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
