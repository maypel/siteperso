from flask import Flask, render_template, jsonify
import json
import requests
# from flask_restful import Api, Resource, abort, reqparse
# from flask_sqlalchemy import SQLAlchemy

# set app et api
app= Flask(__name__)
# api = Api(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)



@app.route("/")
def dashboard():
    return render_template('site.html')

@app.route("/a_propos")
def apropos():
    return render_template('a_propos.html')

if __name__ == "__main__":
    app.run(debug=True)