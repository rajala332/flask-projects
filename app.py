from flask import Flask, request, render_template
app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def weather_data():
    if request.method == 'POST':
        humidity = request.form.get('humidity')
        temperature = request.form.get('temperature')
        rainfall = request.form.get('rainfall')
        return render_template('results.html', humidity=humidity, temperature=temperature, rainfall=rainfall)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)