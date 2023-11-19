import mysql.connector
from flask import render_template

cnx = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='test',
    database='urls'
)

def add_url(url):
    if get_url(url['shorturl']) != 'No Results':
        return render_template('url_exists.html')

    cursor = cnx.cursor()
    insert_query = "INSERT INTO urls (shorturl, longurl) VALUES (%s, %s)"
    data_to_insert = (url['shorturl'], url['longurl'])
    cursor.execute(insert_query, data_to_insert)
    cnx.commit()
    cursor.close()
    return render_template('success.html')

def get_url(url):
    cursor = cnx.cursor()
    query = "SELECT longurl FROM urls WHERE shorturl = '"+url+"'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    if result:
        longurl = result[0]
        print("Long URL:", longurl)
        return longurl
    else:
        print("No matching record found.")
        return 'No Results'