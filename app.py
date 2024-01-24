from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure your database connection
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'redcross'
app.config['MYSQL_PORT'] = 3306  # Specify the correct port

mysql = MySQL(app)


# API endpoint to add data to Bloedvoorraden table
@app.route('/api/add_bloedvoorraden', methods=['POST'])
def add_bloedvoorraden():
    try:
        # Get data from the request
        data = request.json
        bloedzakje_id = data['Bloedzakje_ID']
        bloedgroep = data['Bloedgroep']
        volume = data['Volume']
        verzamelingsdatum = data['Verzamelingsdatum']
        vervaldatum = data['Vervaldatum']

        # Create a cursor and execute the SQL query
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Bloedvoorraden (Bloedzakje_ID, Bloedgroep, Volume, Verzamelingsdatum, Vervaldatum) VALUES (%s, %s, %s, %s, %s)",
            (bloedzakje_id, bloedgroep, volume, verzamelingsdatum, vervaldatum)
        )

        # Commit changes and close the cursor
        mysql.connection.commit()
        cur.close()

        return jsonify({"message": "Data added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route for rendering the HTML template
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
