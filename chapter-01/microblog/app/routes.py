from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/about')
def about():
    return "About Page"

@app.route('/contact')
def contact():
    return "Contact us"