import os
from flask import Flask, jsonify, render_template, request

from TWITOFF.models import db, migrate
from TWITOFF.routes.home_routes import home_routes
from TWITOFF.routes.twitter_routes import twitter_routes
from TWITOFF.routes.admin_routes import admin_routes
from TWITOFF.routes.stats_routes import stats_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")
DATABASE_URL = os.getenv("DATABASE_URL")

def create_app():
    app = Flask(__name__)

    # configure the database
    app.config["SECRET_KEY"] = SECRET_KEY  # allows us to use flash messaging
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    # register routes
    app.register_blueprint(home_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)

    return app
