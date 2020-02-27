from flask import Blueprint, jsonify, request, render_template, flash, redirect

from TWITOFF.models import db

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DB RESET OK"})