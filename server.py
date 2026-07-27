from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pin TEXT UNIQUE,
            category TEXT,
            price REAL,
            status TEXT DEFAULT 'available'
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/add_card', methods=['POST'])
def add_card():
    data = request.json
    pin = data.get('pin')
    category = data.get('category')
    price = data.get('price')
    try:
        conn = sqlite3.connect('cards.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cards (pin, category, price) VALUES (?, ?, ?)", (pin, category, price))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "تم إضافة الكرت بنجاح"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/get_cards', methods=['GET'])
def get_cards():
    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, pin, category, price, status FROM cards")
    cards = cursor.fetchall()
    conn.close()
    return jsonify(cards)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
