from flask import Flask,render_template
import requests  

app= Flask(__name__)
@app.route("/")
def home():
    resp = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=50&minmagnitude=5&latitude=38.9&longitude=35.2&maxradius=10&orderby=magnitude")
    data = resp.json()
    markers = []
    for loc in data["features"]:
        lat, lng, _ = loc["geometry"]["coordinates"]
        marker = {
            "lat": lat,
            "lon": lng,
            "popup": loc["properties"]["title"]
        }
        markers.append(marker)

    return render_template("home.html", markers=markers)
    

if __name__ == '__main__':
    app.run(debug="True",port=8000)
