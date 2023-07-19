#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from models import db, City, Continent, Concities, Food, Blog, User
app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

CORS(app)

api = Api(app)

bcrypt = Bcrypt(app)



# bcrypt.generate_password_hash(password).decode('utf-8')
# bcrypt.check_password_hash(hashed_password, password)

def get_current_user():
    return User.query.where( User.id == session.get("user_id") ).first()

def logged_in():
    return bool( get_current_user() )

# USER SIGNUP #

@app.post('/users')
def create_user():
    json = request.json
    pw_hash = bcrypt.generate_password_hash(json['password']).decode('utf-8')
    new_user = User(username=json['username'], password_hash=pw_hash)
    db.session.add(new_user)
    db.session.commit()
    session['user_id'] = new_user.id
    return new_user.to_dict(), 201



# SESSION LOGIN/LOGOUT#

@app.post('/login')
def login():
    json = request.json
    user = User.query.where(User.username == json["username"]).first()
    if user and bcrypt.check_password_hash(user.password_hash, json['password']):
        session['user_id'] = user.id
        return user.to_dict(), 201
    else:
        return {'message': 'Invalid username or password'}, 401

@app.get('/current_session')
def check_session():
    if logged_in():
        return get_current_user().to_dict(), 200
    else:
        return {}, 401

@app.delete('/logout')
def logout():
    session['user_id'] = None
    return {"message": "Successfully logged out!"}, 204



class Cities(Resource):
    
    def get(self):
        cities = City.query.all()
        response_body = []
        for city in cities:
            response_body.append(city.to_dict())
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_city= City(
                name=data.get('name'),
                image=data.get('image'),
                language=data.get('language'),
                description=data.get('description')
            )
            db.session.add(new_city)
            db.session.commit()
            response_body = new_city.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(Cities, '/cities')

class CityById(Resource):

    def get(self, id):
        city = City.query.filter(City.id == id).first()
        if not city:
            response_body = {'error': 'City not found!'}
            return make_response(jsonify(response_body), 404)
        response_body = city.to_dict()
        continents_list = []
        for continent in city.continents:
            continent_dict = continent.to_dict()
            continents_list.append(continent_dict)
        food_list = [food.to_dict() for food in city.food]
        response_body.update({
            "continents": continents_list,
            "foods": food_list
            })
        return make_response(jsonify(response_body), 200)

    def patch(self, id):
        city = City.query.filter(City.id == id).first()
        if not city:
            response_body = {'error': 'City not found!'}
            return make_response(jsonify(response_body), 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(city, key, data.get(key))
            db.session.commit()
            return make_response(jsonify(city.to_dict()), 202)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

    def delete(self, id):
        city = City.query.filter(City.id == id).first()
        if not city:
            response_body = {'error': 'City not found!'}
            return make_response(jsonify(response_body), 404)
        db.session.delete(city)
        db.session.commit()
        response_body = {}
        return make_response(jsonify(response_body), 204)

api.add_resource(CityById, '/cities/<int:id>')

class Foods(Resource):

    def get(self):
        foods = Food.query.all()
        response_body = []
        for food in foods:
            response_body.append(food.to_dict())
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_food = Food(
                name = data.get('name'),
                image = data.get('image'),
                description = data.get('description'),
                restaurant_recommendation = data.get('restaurant_recommendation'),
                city_id = data.get('city_id')
            )
            db.session.add(new_food)
            db.session.commit()
            response_body = new_food.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)
    
  


api.add_resource(Foods, '/foods')


class FoodsById(Resource):
    def get(self, id):
        food = Food.query.filter(Food.id == id).first()
        if not food:
            response_body = {'error': 'Food not found'}
            return make_response(jsonify(response_body), 404)
        response_body = food.to_dict()
        cities_list = [food.city.to_dict()]
        response_body.update({'cities': cities_list})
        return make_response(jsonify(response_body), 200)

api.add_resource(FoodsById, '/foods/<int:id>')



class Continents(Resource):

    def get(self):
        continents = Continent.query.all()
        response_body = []
        for continent in continents:
            response_body.append(continent.to_dict())
        return make_response(jsonify(response_body), 200)



api.add_resource(Continents, '/continents')

class ContinentsById(Resource):

    def get(self, id):
        continent = Continent.query.filter(Continent.id == id).first()
        if not continent:
            response_body = {'error': 'Continent not found'}
            return make_response(jsonify(response_body), 404)
        response_body = continent.to_dict()
        cities_list = []
        for city in continent.cities:
            city_dict = city.to_dict()
            cities_list.append(city_dict)
        response_body.update({"cities": cities_list})
        return make_response(jsonify(response_body), 200)


api.add_resource(ContinentsById, '/continents/<int:id>')

class Concitiess(Resource):

    def get(self):
        concitiess = Concities.query.all()
        response_body = []
        for concities in concitiess:
            relationship = {
                'city': concities.city.to_dict(),
                'continent': concities.continent.to_dict()
            }
            response_body.append(relationship)
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_concities = Concities(
                city_id = data.get('city_id'),
                continent_id = data.get('continent_id')
            )
            db.session.add(new_concities)
            db.session.commit()
            response_body = new_concities.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)
    
api.add_resource(Concitiess, '/concitiess')

class Blogs(Resource):
    def get(self):
        blogs = Blog.query.all()
        response_body = []
        for blog in blogs:
            response_body.append(blog.to_dict())
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_blog = Blog(
                title = data.get('title'),
                image = data.get('image'),
                blog_post = data.get('blog_post'),
                like_count = data.get('like_count'),
                user_id = data.get('user_id')
            )
            db.session.add(new_blog)
            db.session.commit()
            response_body = new_blog.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)
        
api.add_resource(Blogs,'/blogs')


class BlogsById(Resource):
    def get(self, id):
        blog = Blog.query.filter(Blog.id == id).first()
        if not blog:
            response_body = {'error': 'Blog not found'}
            return make_response(jsonify(response_body), 404)

        response_body = blog.to_dict() if blog else {}
        users_list = [blog.user.to_dict()] if blog.user else []
        response_body.update({'users': users_list})
        return make_response(jsonify(response_body), 200)
    
api.add_resource(BlogsById, '/blogs/<int:id>')




if __name__ == '__main__':
    app.run(port=7001, debug=True)




