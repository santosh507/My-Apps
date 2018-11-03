import flask
from flask import *
from flask import render_template, jsonify
import MySQLdb

# Configuration
app = flask.Flask(__name__)
json_arr=[]

db = MySQLdb.connect(host="localhost",user="root",password="abcd123",database="classicmodels" )

#Model
# Get Orders
with db.cursor() as dbCursor:
    dbCursor.execute('show columns from orders')
    col_hdng = [row[0] for row in dbCursor]
    dbCursor.execute('select * from orders')
    for row in dbCursor:
        json_arr.append(dict(zip(col_hdng,row)))

# Get productLines
    dbCursor.execute('show columns from productlines')
    column_head = [row[0] for row in dbCursor]
    dbCursor.execute('select * from productlines')


# View HomePage
@app.route('/')
def my_homePage():
    return render_template('homepage.html',title='Home Page')


# View Orders
@app.route('/orders')
def my_orders():
    return jsonify(json_arr)


# View ProductLines
@app.route('/productlines')
def product_lines():
    return render_template('productlines.html',productheaders=column_head,
                           title='Product Lines',productline=dbCursor)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)


