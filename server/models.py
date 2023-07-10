from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class City(db.Model, SerializerMixin):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)
    description = db.Column(db.String,nullable=False)

    # food_id = db.Column(db.Integer, db.ForeignKey('foods.id'))

    # Relationships
    concities = db.relationship('Concities', back_populates='city', cascade='all, delete-orphan')
    # food = db.relationship('Food', back_populates='cities')
    food = db.relationship('Food', back_populates='city')
    continents = association_proxy('concities', 'continent', creator=lambda c: Concities(continent=c))

    # Serializer
    serialize_rules = ('-concities', '-food')

    # Validations
    # @validates('number_of_players')
    # def validate_number_of_players(self, key, value):
    #     if not (1 <= int(value) <= 8):
    #         raise ValueError('Number of players must be an integer between 1 and 8.')
    #     return value

    # @validates('release_year')
    # def validate_release_year(self, key, value):
    #     if not (1990 <= int(value) <= 2024):
    #         raise ValueError('Game release year must be a valid year')
    #     return value

    # @validates('description')
    # def validate_description(self, key, value):
    #     if not (25 <= len(value) <= 1000):
    #         raise ValueError('Description must be between 25 and 1000 characters')
    #     return value

    # @validates('genre')
    # def validate_genre(self, key, value):
    #     genres = ['Action', 'Adventure', "Action-Adventure", 'Puzzle', 'RPG', 'Simulator', 'Strategy', 'Sports', 'Shooter', 'Platformer', "Racing", "Horror", "Fighting", "Party", "Stealth", "Sandbox"]
    #     if not value in genres:
    #         raise ValueError(f'{value} is not a valid genre.')
    #     return value

class Continent(db.Model, SerializerMixin):
    __tablename__ = 'continents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    belongs = db.Column(db.String, nullable=False)

    # Relationships
    concities = db.relationship('Concities', back_populates='continent', cascade='all, delete-orphan')
    cities = association_proxy('concities', 'city', creator=lambda c: Concities(city=c))

    # Serializer
    serialize_rules = ('-concities',)

    # Validations
    # @validates('manufacturer')
    # def validate_manufacturer(self, key, value):
    #     types = ['Nintendo', 'Sony', 'Microsoft']
    #     if not value in types:
    #         raise ValueError(f'{key} must be one of the following options: {types}')
    #     return value

    # @validates('type')
    # def validate_type(self, key, value):
    #     types = ['Console', 'Handheld', 'PC']
    #     if not value in types:
    #         raise ValueError(f'{key} must be one of the following options: {types}')
    #     return value
    
class Food(db.Model, SerializerMixin):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    restaurant_recommendation = db.Column(db.String, nullable=False)

    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))


    # Relationships
    # cities = db.relationship('City', back_populates='food', cascade='all, delete-orphan')
    city = db.relationship('City', back_populates='food')
    # Serializer
    serialize_rules = ('-city',)

    # Validations
    # @validates('name')
    # def validate_name(self, key, value):
    #     if not value:
    #         raise ValueError(f'Developer must have a valid {key}.')
    #     return value

class Concities(db.Model, SerializerMixin):
    __tablename__ = 'concities'

    id = db.Column(db.Integer, primary_key=True)
    
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    continent_id = db.Column(db.Integer, db.ForeignKey('continents.id'))

    # Relationships
    city = db.relationship('City', back_populates='concities')
    continent = db.relationship('Continent', back_populates='concities')

    # Serializer
    serialize_rules = ('-city', '-continent')

    # Validations
    # @validates('name', 'game_id', 'device_id')
    # def validate_mission_info(self, key, value):
    #     if not value:
    #         raise ValueError(f'Geedee must have a {key}.')
    #     return value

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False, unique=True)
#     password_hash = db.Column(db.String)

#     def get(self):
#         pass