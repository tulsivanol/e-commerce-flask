# Flask MongoDB E-commerce App

This is a simple Flask application that connects to a MongoDB database and renders products from the database onto a
product page. The application uses Jinja2 for templating and loads MongoDB credentials from environment variables using
`python-dotenv`.

## Features

Home page that renders a basic HTML template.
Product page that fetches a list of products from a MongoDB collection and renders it using Jinja2.
MongoDB connection using `pymongo` with environment variables for credentials.

## Prerequisites

Before running the application, ensure you have the following installed:

Python 3.10
MongoDB Atlas (or any MongoDB instance)
`pip` (Python package installer)

## Setup

### Step 1: Clone the repository

    git clone https://github.com/tulsivanol/e-commerce-flask.git
    cd e-commerce-flask

### Step 2: Install dependencies

    pip install -r requirements.txt

### Step 3: Set up MongoDB Atlas

Create a MongoDB Atlas cluster if you don't already have one.
Set up a database called `shop_db` and a collection called `products`.
Ensure your MongoDB user has the necessary access to the database.
Replace `<Your MongoDB Username>` and `<Your MongoDB Password>` in the `.env` file (see instructions below).

### Step 4: Create a .env file

Create a .env file in the root directory of your project and add the following environment variables:

    MONGODB_USERNAME=<Your MongoDB Username>
    MONGODB_PASSWORD=<Your MongoDB Password>

Example .env file:

    MONGODB_USERNAME=myMongoDBUser
    MONGODB_PASSWORD=myStrongPassword

### Step 5: Directory Structure

Ensure the project has the following structure:

    _/app
    │
    ├── /templates
    │ ├── home.html
    │ ├── products.html
    │
    ├── app.py
    ├── .env
    ├── requirements.txt_

- `home.html`: A simple HTML file to be rendered on the home page.
- `products.html`: HTML template to display the list of products from the MongoDB database.
- `.env`: Contains environment variables for MongoDB credentials.

### Step 6: Run the Application

Run the Flask application using the following command:

    python app.py

By default, the Flask app will run on `http://127.0.0.1:5000/`.

#### Endpoints

##### 1. Home Page:

URL: `/`
Renders `home.html`.

##### 2. Products Page:

URL: `/products`
Fetches the list of products from the `products` collection in MongoDB and renders them using the `products.html`
template.

### Step 7: Verify MongoDB Connection

When you run the application, you should see the following output in your terminal:

    Pinged your deployment. You successfully connected to MongoDB!

If there are issues with the connection, an error message will be displayed.

### Dependencies

The application requires the following Python libraries:

`Flask`: Web framework.
`pymongo`: MongoDB driver for Python.
`python-dotenv`: For loading environment variables from a .env file.
`Jinja2`: Templating engine for Flask.
These are included in the requirements.txt file. To install them, simply run:

    pip install -r requirements.txt

### Troubleshooting

- Invalid MongoDB credentials: Ensure that the MongoDB username and password in the .env file are correct.
- MongoDB connection error: Check that your MongoDB Atlas instance is running and that your IP is whitelisted for access.