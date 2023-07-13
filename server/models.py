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
    description = db.Column(db.String, nullable=False)


    # Relationships
    concities = db.relationship('Concities', back_populates='city', cascade='all, delete-orphan')
    # food = db.relationship('Food', back_populates='cities')
    food = db.relationship('Food', back_populates='city')


    continents = association_proxy('concities', 'continent', creator=lambda c: Concities(continent=c))

    # Serializer
    serialize_rules = ('-concities', '-food')



    # @validates('description')
    # def validate_description(self, key, value):
    #     if not (25 <= len(value) <= 1000):
    #         raise ValueError('Description must be between 25 and 1000 characters')
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

    # # Validations
    # @validates('belongs')
    # def validate_manufacturer(self, key, value):
    #     conts = ['Europe', 'Asia', 'Africa', 'Australia and Ocenia', 'North America', 'South America']
    #     if not value in conts:
    #         raise ValueError(f'{key} must be one of the following options: {conts}')
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
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError(f'Food must have a valid {key}.')
        return value

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
    @validates('city_id', 'continent_id')
    def validate_concities_info(self, key, value):
        if not value:
            raise ValueError(f'Concities must have a {key}.')
        return value


class Blog(db.Model, SerializerMixin):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    blog_post = db.Column(db.String, nullable=False)
    like_count = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#Relationships
    user = db.relationship('User', back_populates='blogs')


#Serializer
    serialize_rules = ('-user',)

    

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash= db.Column(db.String)
    
    def __repr__(self):
        return f'<User id="{self.id}" username="{self.username}">'
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "pw": self.password_hash
        }
#Relationships
    blogs = db.relationship('Blog', back_populates='user')

#Serializer
    serialize_rules = ('-blogs',)

