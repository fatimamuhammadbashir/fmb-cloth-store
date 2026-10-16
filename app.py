
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Welcome to FMB Cloth Store!</h1>
    <h2>Your Style, Your Choice.</h2>
    <p>We sell Abaya, Dresses, Atamfa, Shadda, Shoes and Bags.</p>
    <p>Our first product is Abaya.</p>
    <p>Price: ₦25,000</p>
    <p>Stock: 10 pieces</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
  
