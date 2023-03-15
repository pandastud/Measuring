from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:DeAdPoOl2001@localhost:3306/diploma_schema'
db = SQLAlchemy(app)
cors = CORS(app)


class OxygenData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    oxygen_level = db.Column(db.Float, nullable=False)


@app.route('/api/oxygen')
@cross_origin()
def get_oxygen_data():
    oxygen_data = OxygenData.query.all()
    result = [{'id': o.id, 'timestamp': o.timestamp, 'oxygen_level': o.oxygen_level} for o in oxygen_data]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
