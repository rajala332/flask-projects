from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')
stations = {
    "Bhubaneswar": 0,
    "Cuttack": 25,
    "Puri": 60,
    "Balasore": 150,
    "Berhampur": 180
}
price_per_km = 1  
seat_number = 1 
@app.route('/')
def home():
    return render_template("index.html", stations=stations.keys())
@app.route('/calculate', methods=['POST'])
def calculate():
    source = request.form['source']
    destination = request.form['destination']

    if source == destination:
        return render_template("index.html", stations=stations.keys(), 
                               message="Source and Destination cannot be same!")
    distance = abs(stations[destination] - stations[source])
    cost = distance * price_per_km

    return render_template("index.html", stations=stations.keys(),
                           cost=cost,
                           source=source,
                           destination=destination,
                           seat=f"S-{seat_number}")
if __name__ == '__main__':
    app.run(debug=True)