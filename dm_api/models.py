from dm_api import db

class User(db.Model):
	id = db.Column(db.String(12), primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	role = db.Column(db.String(50), nullable=False)
	points = db.Column(db.Integer, nullable=False)