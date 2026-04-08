from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import csv

from database import get_db_connection
from risk_engine import calculate_risk, get_status
from email_alert import configure_mail, send_alert_email


app = Flask(__name__)
CORS(app)

# configure gmail alert system
mail = configure_mail(app)


# ===============================
# DATABASE INITIALIZATION
# ===============================

def initialize_database():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        profile_image TEXT,
        risk_score INTEGER DEFAULT 0,
        status TEXT DEFAULT 'Real'
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count == 0:

        try:

            with open("user_sample.csv", "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    cursor.execute(
                        """
                        INSERT INTO users
                        (username, email, profile_image, risk_score, status)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (row["username"], row["email"], "", 0, "Real")
                    )

        except:

            print("Sample CSV not found")

    conn.commit()
    conn.close()

    print("Database initialized successfully")


# ===============================
# REGISTER USER WITH DETECTION ENGINE + EMAIL ALERT
# ===============================

@app.route("/register-user", methods=["POST"])
def register_user():

    data = request.json

    if not data:

        return jsonify({"error": "No data received"}), 400

    username = data.get("username")
    email = data.get("email")

    if not username or not email:

        return jsonify({"error": "Username and email required"}), 400


    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT username, email FROM users")

    existing_users = cursor.fetchall()


    risk_score, matches = calculate_risk(username, existing_users)

    status = get_status(risk_score)


    # ===============================
    # EMAIL ALERT LOGIC
    # ===============================

    if matches:

        highest_similarity = max(match["similarity"] for match in matches)

        if highest_similarity >= 90:

            original_email = matches[0]["email"]
            original_username = matches[0]["username"]

            send_alert_email(
                mail,
                app.config['MAIL_USERNAME'],
                original_email,
                original_username,
                username
            )


    # ===============================
    # SAVE USER
    # ===============================

    cursor.execute(
        """
        INSERT INTO users
        (username, email, profile_image, risk_score, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (username, email, "", risk_score, status)
    )

    conn.commit()
    conn.close()


    return jsonify({

        "message": "User registered successfully",
        "riskScore": risk_score,
        "status": status,
        "matches": matches
    })


# ===============================
# MONITOR USERNAME SIMILARITY
# ===============================

@app.route("/monitor-username", methods=["POST"])
def monitor_username():

    data = request.json

    username = data.get("username", "")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT username, email FROM users")

    existing_users = cursor.fetchall()

    risk_score, matches = calculate_risk(username, existing_users)

    conn.close()


    if matches:

        return jsonify({

            "alert": True,
            "matches": matches
        })


    return jsonify({

        "alert": False
    })


# ===============================
# RUN SERVER
# ===============================

if __name__ == "__main__":

    initialize_database()

    app.run(debug=True)