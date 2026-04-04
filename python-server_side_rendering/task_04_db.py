# task_03_files.py
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_csv_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = {
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            }
            products.append(product)
    return products

def read_sql_database():

    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            product = {
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            }
            products.append(product)
        
        conn.close()
        return products
    
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             products=None, 
                             error="Wrong source")
    
    try:
        if source == 'json':
            products = read_json_file('products.json')
        elif source == 'csv':
            products = read_csv_file('products.csv')
        elif source == 'sql':
            products = read_sql_database()
    except FileNotFoundError:
        return render_template('product_display.html', 
                             products=None, 
                             error="Data file not found")
    except Exception as e:
        return render_template('product_display.html', 
                             products=None, 
                             error=str(e))

    if product_id is not None:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p['id'] == product_id]
            
            if not filtered:
                return render_template('product_display.html', 
                                     products=None, 
                                     error="Product not found")

            products = filtered
        except ValueError:
            return render_template('product_display.html', 
                                 products=None, 
                                 error="Invalid id format")
    
    return render_template('product_display.html', products=products, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
