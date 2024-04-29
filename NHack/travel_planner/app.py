from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to fetch attractions based on user interests
def get_attractions_by_interests(interests):
    conn = sqlite3.connect('tourism.db')
    cursor = conn.cursor()

    attractions = []
    for interest in interests:
        cursor.execute('''SELECT state, attractions FROM attractions
                          WHERE attractions LIKE ?''', ('%' + interest.strip() + '%',))
        attractions.extend(cursor.fetchall())

    conn.close()
    return attractions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_interests = request.form.get('interests').split(',')
    attractions = get_attractions_by_interests(user_interests)
    return render_template('results.html', attractions=attractions)

if __name__ == '__main__':
    app.run(debug=True)
