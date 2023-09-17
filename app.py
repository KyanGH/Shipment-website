from flask import Flask, render_template, request, redirect, url_for
import MyDB

app = Flask(__name__)

@app.route('/login.html', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    connection = MyDB.create_connection()
    if connection:
        cursor = connection.cursor()

        if MyDB.authenticate_user(connection, cursor, username, password):
            cursor.close()
            connection.close()
            # Redirect to the "index.html" page on successful login
            return redirect(url_for('index'))  # Assuming 'index' is the route for "index.html"

        cursor.close()
        connection.close()

    return "Login failed. Please check your credentials."

@app.route('/index.html')
def index():
    # You can add any logic for your "index.html" page here
    return render_template('index.html')  # Assuming you're using Flask's render_template to render HTML templates

if __name__ == '__main__':
    app.run(debug=True)
