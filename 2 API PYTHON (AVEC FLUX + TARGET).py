from flask import Flask, jsonify
import psycopg2
import geoip2.database

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="gestion_ecole",
    user="postgres",
    password="mot_de_passe"
)

reader = geoip2.database.Reader('/usr/share/GeoIP/GeoLite2-City.mmdb')

TARGET = (-1.67, 29.22)

def geo(ip):
    try:
        r = reader.city(ip)
        return r.location.latitude, r.location.longitude
    except:
        return 0,0

@app.route("/map")
def map_data():
    cur = conn.cursor()
    cur.execute("SELECT ip, risk_score FROM security_risk_log ORDER BY created_at DESC LIMIT 100")

    out = []
    for ip, score in cur.fetchall():
        lat, lon = geo(ip)

        out.append({
            "from": [lat, lon],
            "to": TARGET,
            "score": score
        })

    return jsonify(out)

app.run(host="0.0.0.0", port=5000)
