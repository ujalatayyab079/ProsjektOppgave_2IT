from flask import Flask, render_template, session, request, jsonify  # Importerer Flask
import mysql.connector  # For å koble til databasen
from dotenv import load_dotenv
import os

app = Flask(__name__)  # Lager selve nettsiden
app.secret_key = "secret07"  # Viktig for session


# Leser sensitiv info fra .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Kobling til MariaDB
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
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

@app.route("/faq")
def faq():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM faq ORDER BY category, id")
    faqs = cursor.fetchall()
    cursor.close()
    return render_template("faq.html", faqs=faqs)

#--- Handelkurv og favorit ikon----
@app.before_request
def make_session_lists():
    if "favorites" not in session:
        session["favorites"] = []
    if "cart" not in session:
        session["cart"] = []

@app.route("/toggle_favorite", methods=["POST"])
def toggle_favorite():
    product_id = request.json.get("product_id")
    if product_id in session["favorites"]:
        session["favorites"].remove(product_id)
        action = "removed"
    else:
        session["favorites"].append(product_id)
        action = "added"
    session.modified = True
    return jsonify({"status": "success", "action": action, "favorites": session["favorites"]})

@app.route("/toggle_cart", methods=["POST"])
def toggle_cart():
    product_id = request.json.get("product_id")
    if product_id in session["cart"]:
        session["cart"].remove(product_id)
        action = "removed"
    else:
        session["cart"].append(product_id)
        action = "added"
    session.modified = True
    return jsonify({"status": "success", "action": action, "cart": session["cart"]})



if __name__=="__main__":  #Kodem kan kun kjøres ved filen app.py men ikke direkte.
    app.run(debug=True)  # Nettserveren på  datamaskinen

