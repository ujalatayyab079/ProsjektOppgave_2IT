from flask import Flask, render_template  # Importerer Flask
import mysql.connector  #for å koble til databasen, hente produkter, lagre handlekurv osv

app = Flask(__name__)  #lager selve nettsiden

#Kobling til MariaDB
db = mysql.connector.connect(    #Lager en kobling til databasen
    host="192.168.0.112",
    user="ujala_2025",
    password="pakistan07",
    database="shinystar_shop"
)

@app.route('/')   #Kjør funsksjon under
def home():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products LIMIT 4") #Dette er SQL-spørringen til databasen.
    products = cursor.fetchall()  #Lager resultate
    cursor.close()
    return render_template('home.html', products=products)

@app.route('/products')
def products():
    cursor = db.cursor(dictionary=True) # dictionary=True gjør at vi får kolonnenavn som nøkler
    cursor.execute("SELECT * FROM products") #Henter alle produkter
    products = cursor.fetchall() #Lagrer resultatet
    cursor.close()
    return render_template('products.html' , products=products)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')



if __name__=="__main__":  #Kodem kan kun kjøres ved filen app.py men ikke direkte.
    app.run(debug=True)  # Nettserveren på  datamaskinen

