from flask import Flask, render_template, request, jsonify, redirect, url_for, g, flash
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'tomb-tomb-tomb-sahoor'

# Points throughout ALL games


#
#
# Creates all necessary databases, the querstions, and the users database
#
#

gw_points = 0
curr_name = "New Buddy!!"

# Home route that renders index.html


@app.route('/')
def home():
    return render_template('/index.html', name=curr_name)


def get_user_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/login', methods=['GET', 'POST'])
def login():
    global curr_user
    global curr_name
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = get_user_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE email = ? AND name = ? AND password = ?', (email, name, password)).fetchone()
        conn.close()

        if user:
            curr_id = user['id']
            curr_name = user['name']
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid name, email, or password.')

    return render_template('login.html')


# Entire section dedicated to the test function '

# Connect to DB
def get_questions_db():
    if '_database' not in g:
        g._database = sqlite3.connect('questions.db')
        g._database.row_factory = sqlite3.Row  # For dict-like row access
    return g._database

# Close DB connection


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/test')
def test():

    db = get_questions_db()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM questions LIMIT 1")
        row = cursor.fetchone()
    except sqlite3.Error as e:
        return render_template('test.html', error=f"DB error: {e}")

    if row:
        question_data = {
            'question': row['question'],
            'answers': [
                {'text': row['answer1'], 'correct': row['is1correct']},
                {'text': row['answer2'], 'correct': row['is2correct']},
                {'text': row['answer3'], 'correct': row['is3correct']},
            ]
        }
        return render_template('test.html', points=gw_points, question=question_data)
    else:
        exq = {
            'question': "How many continents are there?",
            'answers': [
                {'text': "7", 'correct': 1},
                {'text': "3", 'correct': 0},
                {'text': "13", 'correct': 0},
            ]
        }
        return render_template('test.html', question=exq, points=gw_points, error="No questions found")

# def next_row_test():


@app.route('/match')
def match():
    return render_template('/match.html')


@app.route('/sprint')
def sprint():
    return render_template('/sprint.html')


@app.route('/learn')
def learn():
    return render_template('/learn.html')

# Example form handler


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form.get('data')
        return f"Received: {data}"
    return '''
        <form method="post">
            <input name="data">
            <input type="submit">
        </form>
    '''

# Example API route


@app.route('/api/data', methods=['POST'])
def api_data():
    json_data = request.get_json()
    return jsonify({"you_sent": json_data})


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            with sqlite3.connect("users.db") as conn:
                conn.execute(
                    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                    (name, email, password)
                )
            flash("Success!")
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            flash("Incorrect Input")
            return render_template("/signup.html", error="Email already exists. Try logging in.")

    return render_template("/signup.html")


@app.route('/increment')
def increase_gw_points():
    gw_points += 1
    db = get_questions_db()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM questions LIMIT 1", (gwpoints,))
        row = cursor.fetchone()
    except sqlite3.Error as e:
        return render_template('test.html', error=f"DB error: {e}")

    if row:
        question_data = {
            'question': row['question'],
            'answers': [
                {'text': row['answer1'], 'correct': row['is1correct']},
                {'text': row['answer2'], 'correct': row['is2correct']},
                {'text': row['answer3'], 'correct': row['is3correct']},
            ]
        }
        return render_template('test.html', question=question_data)
    else:
        exq = {
            'question': "How many continents are there?",
            'answers': [
                {'text': "7", 'correct': 1},
                {'text': "3", 'correct': 0},
                {'text': "13", 'correct': 0},
            ]
        }
        return render_template('test.html', question=exq, points=gw_points, error="No questions found")


if __name__ == '__main__':
    init_users_db()
    init_questions_db()
    app.run(debug=True)
