from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from jinja2 import Environment, PackageLoader, select_autoescape
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

app = Flask(__name__)

# Html template setup
env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape()
)

# MongoDB Connection URL
uri = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@ecommercecluster.sonrn.mongodb.net/?retryWrites=true&w=majority&appName=ECommerceCluster"

# Database connection
client = MongoClient(uri, server_api=ServerApi('1'))
shop_db = client['shop_db']
product_col = shop_db['products']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Home page (/)
@app.route('/')
def home():  # put application's code here
    template = env.get_template('home.html')
    return template.render()


# Product page (/products)\
@app.route("/products")
def products():
    template = env.get_template('products.html')
    product_list = product_col.find()
    return template.render(products=product_list)


if __name__ == '__main__':
    app.run()