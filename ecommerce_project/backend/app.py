from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(["Phones", "Clothing", "Accessories", "Footwear"])

@app.route('/products')
def get_products():
    products = [
        # Smartphones
        {"ProductID": 1, "Name": "iPhone 14", "Category": "Smartphone", "Price": 54999, "ImageURL": "images/iphone14.jpeg"},
        {"ProductID": 2, "Name": "Samsung Galaxy S22", "Category": "Smartphone", "Price": 72999, "ImageURL": "images/galaxy_s22.jpeg"},
        {"ProductID": 3, "Name": "One Plus 12", "Category": "Smartphone", "Price": 54990, "ImageURL": "images/op_12.jpeg"},
        {"ProductID": 4, "Name": "Realme 13 Pro", "Category": "Smartphone", "Price": 26999, "ImageURL": "images/rm_13.jpeg"},
        {"ProductID": 5, "Name": "Moto g85", "Category": "Smartphone", "Price": 16999, "ImageURL": "images/mg_85.jpeg"},

        # T-Shirts
        {"ProductID": 6, "Name": "Black Cotton T-Shirt", "Category": "T-shirt", "Price": 250, "ImageURL": "images/black.jpeg"},
        {"ProductID": 7, "Name": "White T-Shirt", "Category": "T-shirt", "Price": 300, "ImageURL": "images/white.jpeg"},
        {"ProductID": 8, "Name": "Polo T-Shirt", "Category": "T-shirt", "Price": 450, "ImageURL": "images/polo.jpeg"},
        {"ProductID": 9, "Name": "Over-Size T-Shirt", "Category": "T-shirt", "Price": 500, "ImageURL": "images/oversize.jpeg"},
        {"ProductID": 10, "Name": "Sport T-Shirt", "Category": "T-shirt", "Price": 200, "ImageURL": "images/sport.jpeg"},

        # Watches
        {"ProductID": 11, "Name": "Minimalist Slim Series", "Category": "Watch", "Price": 2270, "ImageURL": "images/blackw.jpeg"},
        {"ProductID": 12, "Name": "Tiffany Treasure Women's Quartz Watch", "Category": "Watch", "Price": 3000, "ImageURL": "images/tiffany.jpeg"},
        {"ProductID": 13, "Name": "G-SHOCK Analog-Digital Watch", "Category": "Watch", "Price": 49990, "ImageURL": "images/gsw.jpeg"},
        {"ProductID": 14, "Name": "Regalia Ceramic 3 Analog Watch", "Category": "Watch", "Price": 19945, "ImageURL": "images/titan.jpeg"},
        {"ProductID": 15, "Name": "Tik Tock 4 Analog Watch", "Category": "Watch", "Price": 4195, "ImageURL": "images/fastrack.jpeg"},

        # Shoes
        {"ProductID": 16, "Name": "Nike Running Shoes", "Category": "Shoes", "Price": 3999, "ImageURL": "images/nike.jpeg"},
        {"ProductID": 17, "Name": "Adidas Sneakers", "Category": "Shoes", "Price": 3499, "ImageURL": "images/adidas.jpeg"},
        {"ProductID": 18, "Name": "Puma Sports Shoes", "Category": "Shoes", "Price": 3299, "ImageURL": "images/puma.jpeg"},
        {"ProductID": 19, "Name": "Woodland Boots", "Category": "Shoes", "Price": 4599, "ImageURL": "images/woodland.jpeg"},
        {"ProductID": 20, "Name": "Sparx Casual Shoes", "Category": "Shoes", "Price": 1499, "ImageURL": "images/sparx.jpeg"},

        # Flip-Flops
        {"ProductID": 21, "Name": "Puma Flip-Flops", "Category": "Flip-Flops", "Price": 499, "ImageURL": "images/pumaflip.jpeg"},
        {"ProductID": 22, "Name": "Sparx Flip-Flops", "Category": "Flip-Flops", "Price": 399, "ImageURL": "images/sparxflip.jpeg"},
        {"ProductID": 23, "Name": "Adidas Slides", "Category": "Flip-Flops", "Price": 599, "ImageURL": "images/adidasslide.jpeg"},
        {"ProductID": 24, "Name": "Nike Flip-Flops", "Category": "Flip-Flops", "Price": 699, "ImageURL": "images/nikeslide.jpeg"},
        {"ProductID": 25, "Name": "Crocs Flip-Flops", "Category": "Flip-Flops", "Price": 999, "ImageURL": "images/crocs.jpeg"},

        # Sandals
        {"ProductID": 26, "Name": "Bata Sandals", "Category": "Sandals", "Price": 799, "ImageURL": "images/bata.jpeg"},
        {"ProductID": 27, "Name": "Relaxo Sandals", "Category": "Sandals", "Price": 699, "ImageURL": "images/relaxo.jpeg"},
        {"ProductID": 28, "Name": "Campus Sandals", "Category": "Sandals", "Price": 599, "ImageURL": "images/campus.jpeg"},
        {"ProductID": 29, "Name": "Paragon Sandals", "Category": "Sandals", "Price": 499, "ImageURL": "images/paragon.jpeg"},
        {"ProductID": 30, "Name": "Red Tape Sandals", "Category": "Sandals", "Price": 999, "ImageURL": "images/redtape.jpeg"},
    ]
    return jsonify(products)

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.get_json()
    cart = data.get('cart', [])
    payment_mode = data.get('payment_mode', '')

    if not cart or not payment_mode:
        return jsonify({"message": "Invalid order data"}), 400

    print("Received order:", cart)
    print("Payment mode:", payment_mode)

    return jsonify({"message": "Order placed successfully!"}), 200
@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)