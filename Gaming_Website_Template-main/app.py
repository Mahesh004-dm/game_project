from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for category pages
@app.route('/category/<category_name>')
def category(category_name):
    return render_template('categoryGame.html', category_name=category_name)

# Route for creating a post
@app.route('/create')
def create_post():
    return render_template('create.html')

# Route for the profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Route for game details page
@app.route('/game/<game_id>')
def game_details(game_id):
    return render_template('gameDetails.html', game_id=game_id)

# Route for login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for registration page
@app.route('/register')
def register():
    return render_template('register.html')

# Start the app
if __name__ == '__main__':

    app.run(host="127.0.0.1",
            port=5006,
            debug=True)

