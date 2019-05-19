from flask import Blueprint, jsonify, request
from dm_api import db
from .models import User


main = Blueprint('main', __name__)


@main.route('/users/add', methods=['POST'])
def add_user():
	user_data = request.get_json()

	new_user = User(id=user_data['id'], 
					name=user_data['name'], 
					role=user_data['role'], 
					points=user_data['points']
					)

	db.session.add(new_user)
	db.session.commit()

	return 'Done', 201


@main.route('/users', methods=['GET'])
def users():
	user_list = User.query.all()
	users = []

	for user in user_list:
		users.append({'id': user.id,
					 'name': user.name,
					 'role': user.role,
					 'points': user.points})

	return jsonify({'users' : users})

@main.route('/users/delete', methods=['POST'])
def delete_user():
	user = request.get_json()

	user_to_delete = User.query.get_or_404(user['id'])

	db.session.delete(user_to_delete)
	db.session.commit()

	return f'user has been deleted...', 201