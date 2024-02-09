from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/products.html', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        # This block will execute when a POST request is made to /products.html
        # Here you capture the "Shop Now" event
        print("Shop Now event captured!")
        # You can access form data using request.form
        print("Data received:", request.form)
        # You can handle the event further (e.g., store in a database, process payment, etc.)
        return "Shop Now event captured!"
    else:
        # This block will execute when a GET request is made to /products.html
        # Here you render the products page
        return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
