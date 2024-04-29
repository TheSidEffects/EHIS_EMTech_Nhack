import sqlite3

def create_database():
    # Data to be inserted into the database
    attractions_data = [
        ('Andhra Pradesh', 'Tirupati temples, jyotirlinga temples'),
        ('Arunachal Pradesh', 'mountains, streams'),
        ('Assam', 'rivers, wildlife, tea plantation, temples'),
        ('Bihar', 'sacred places for Hindu, Muslim, Buddhism. Pilgrimage temples'),
        ('Chhattisgarh', 'waterfalls, forest, plateau, temples'),
        ('Goa', 'nightlife, beaches, wildlife'),
        ('Gujarat', 'beaches, temples, historic places, handicrafts'),
        ('Haryana', 'greenery, temples, attractive architecture'),
        ('Himachal Pradesh', 'landscape, hill stations'),
        ('Jharkhand', 'rich culture and heritage, moderate climate, religious places'),
        ('Karnataka', 'wildlife, national parks, hill station'),
        ('Kerala', 'backwaters, demography'),
        ('Maharashtra', 'ancient cave temples, forts, monuments, hill stations'),
        ('Madhya Pradesh', 'temples, forts, palaces'),
        ('Manipur', 'scenic beauty, wildlife'),
        ('Meghalaya', 'monsoon, forest'),
        ('Mizoram', 'hills, forest'),
        ('Nagaland', 'landscape'),
        ('Odisha', 'historical junctures, scenery'),
        ('Punjab', 'holiest places'),
        ('Rajasthan', 'deserts, forts, palaces'),
        ('Sikkim', 'temples'),
        ('Tamil Nadu', 'beach, hill, mountain, wildlife'),
        ('Tripura', 'temples, sculptures'),
        ('Telangana', 'handicrafts, sculptures'),
        ('Uttar Pradesh', 'attractive sculptures'),
        ('Uttarakhand', 'mountains, vibrant culture, temples, rivers'),
        ('West Bengal', 'temple, mosque, church'),
        ('Andaman & Nicobar (UT)', 'evergreen forest, wildlife'),
        ('Chandigarh (UT)', 'architecture, lakes'),
        ('Dadra & Nagar Haveli and Daman & Diu (UT)', 'river'),
        ('Delhi [National Capital Territory (NCT)]', 'historical and architecture heritage'),
        ('Jammu & Kashmir (UT)', 'mountains, lakes, temples'),
        ('Ladakh (UT)', 'war memorials, temples'),
        ('Lakshadweep (UT)', 'scenic charm'),
        ('Puducherry (UT)', 'beaches and backwaters')
    ]

    # Connect to SQLite database
    conn = sqlite3.connect('tourism.db')
    cursor = conn.cursor()

    # Create attractions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS attractions
                    (state TEXT PRIMARY KEY, attractions TEXT)''')

    # Insert data into attractions table
    cursor.executemany('''INSERT OR IGNORE INTO attractions (state, attractions)
                          VALUES (?, ?)''', attractions_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("SQLite database created and populated successfully.")

if __name__ == '__main__':
    create_database()

