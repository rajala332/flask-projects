from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        size = float(request.form['size'])
        bedrooms = int(request.form['bedrooms'])
        location = int(request.form['location'])
        location_bonus = {1: 500000, 2: 300000, 3: 100000}
        price = (size * 1500) + (bedrooms * 10000) + location_bonus.get(location, 0)

        return render_template('index.html', prediction=round(price, 2))

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)