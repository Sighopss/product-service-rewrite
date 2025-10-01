"""
Product Service - Python Flask Application
A simple web service that serves a product catalog via RESTful API.
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Configure CORS to allow cross-origin requests
CORS(app, resources={
    r"/products": {
        "origins": "*",
        "methods": ["GET"],
        "allow_headers": ["Content-Type"]
    },
    r"/products/*": {  # Add CORS for /products/<id>
        "origins": "*",
        "methods": ["GET"],
        "allow_headers": ["Content-Type"]
    },
    r"/health": {
        "origins": "*",
        "methods": ["GET"],
        "allow_headers": ["Content-Type"]
    }
})

# Sample product data
PRODUCTS = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99}
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    GET /products endpoint
    Returns a JSON array of product objects
    """
    return jsonify(PRODUCTS)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    GET /products/<id> endpoint
    Returns a single product by ID or 404 if not found
    """
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring
    """
    return jsonify({"status": "healthy", "service": "product-service"})

if __name__ == '__main__':
    # Get port from environment variable or default to 3030
    port = int(os.environ.get('PORT', 3030))
    
    # Run the application
    app.run(
        host='0.0.0.0',  # Bind to all interfaces (12-Factor App compliance)
        port=port,
        debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    )
