from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:DeAdPoOl2001@localhost:3306/diploma_schema'
db = SQLAlchemy(app)


class OxygenSensor(db.Model):
    __tablename__ = 'oxygen_data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    oxygen_level = db.Column(db.Float, nullable=False)


@app.route('/oxygen')
def oxygen_data():
    results = OxygenSensor.query.all()
    readings = []
    for result in results:
        oxygen_level = {
            'timestamp': result.timestamp,
            'oxygen_level': result.oxygen_level
        }
        readings.append(oxygen_level)
    return jsonify(readings)


if __name__ == '__main__':
    app.run(debug=True)
