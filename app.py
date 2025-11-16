from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# CORS aberto para o Frame
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept", "User-Agent"],
        "supports_credentials": False
    }
})

# Dados mockados para teste
MOCK_PRODUCTS = [
    {
        "id": 1,
        "name": "Produto Exemplo 1",
        "current_stock": 100,
        "unit_cost": 15.50,
        "category": "Eletrônicos"
    },
    {
        "id": 2,
        "name": "Produto Exemplo 2",
        "current_stock": 50,
        "unit_cost": 25.00,
        "category": "Material de Escritório"
    }
]

@app.route('/api/products', methods=['GET'])
def get_products():
    """Endpoint público para o Frame"""
    return jsonify({
        "data": MOCK_PRODUCTS,
        "message": "Products retrieved successfully"
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "message": "API is running"
    }), 200

@app.route('/')
def index():
    return jsonify({
        "message": "Inventory API for Frame",
        "endpoints": ["/api/products", "/health"]
    })

if __name__ == "__main__":
    # Tentar porta 8080 primeiro, se não 5000
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=False)