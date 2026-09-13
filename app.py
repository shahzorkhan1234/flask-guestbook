"""
Guestbook backend.
This is the "server" — it runs Python, talks to the database,
and sends HTML back to the browser.
"""
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = "guestbook.db"


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # lets us use column names
    return conn


def setup():
    # Make the table the first time. A table is like a spreadsheet:
    # each row is one signature, with an id, a name, and a message.
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS signatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    # Read every signature, newest first, and hand them to the page.
    conn = get_db()
    rows = conn.execute(
        "SELECT name, message FROM signatures ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return render_template("index.html", signatures=rows)


@app.route("/sign", methods=["POST"])
def sign():
    # This runs when someone submits the form.
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()
    if name:  # only save if they typed a name
        conn = get_db()
        conn.execute(
            "INSERT INTO signatures (name, message) VALUES (?, ?)",
            (name, message),
        )
        conn.commit()
        conn.close()
    return redirect("/")  # reload the page to show the new signature


if __name__ == "__main__":
    setup()
    app.run(debug=True)
