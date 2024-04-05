from flask import Flask, render_template, redirect, url_for, request
import requests
import os
import sqlite3
import json

def getProducts():
    # Get the directory of the current Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Specify the relative path to the SQLite database file
    database_relative_path = 'database/nutrimet_db.db'
    database_file = os.path.join(current_directory, database_relative_path)

    # Establish a connection to the SQLite database file
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    # # Define the data to be inserted
    # data = {
    #     'c_productid': 'gym_2',
    #     'c_productname': "Weightlifting Gloves",
    #     'c_productdescription': "Durable gloves with wrist support for a comfortable grip during workouts",
    #     'c_originalprice': 30,
    #     'c_discountedprice': 20,
    #     'c_isondiscount': 1,
    #     'c_imageurl': "https://images.stockcake.com/public/1/7/c/17c3e09a-5fb4-467b-95c4-6cfe48d5faab_large/gym-workout-equipment-stockcake.jpg"
    # }
    # # Construct the INSERT query
    # query = """
    # INSERT INTO t_products (c_productid, c_productname, c_productdescription, c_originalprice, c_discountedprice, c_isondiscount, c_imageurl)
    # VALUES (:c_productid, :c_productname, :c_productdescription, :c_originalprice, :c_discountedprice, :c_isondiscount, :c_imageurl)
    # """

    # # Execute the query
    # cursor.execute(query, data)

    # # Commit the transaction
    # connection.commit()

    # Get Product Data
    cursor.execute('SELECT * FROM t_products')
    rows = cursor.fetchall()

    # print(rows)

    # Close connection
    connection.close()

    # Store data from db in an array
    products = []
    for row in rows:
        products.append(row)

    print(products)
    return products

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    product_data = getProducts()

    # Convert the data to JSON format
    json_data = json.dumps(product_data, indent=4)

    return render_template('index.html', product_data = json_data)

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('html/aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)