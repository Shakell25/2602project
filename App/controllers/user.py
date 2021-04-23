from flask import redirect, render_template, request, session, url_for

from App.models import ( User )

def get_users_jason():
    users = User.query.all()
    if not users:
        return jsonify([])
    json = [user.toDict() for user in users]
    return json

def create_user(firstname, lastname, uwi_id, email, gender, dob):
    # newuser = use()
    return 'new user'