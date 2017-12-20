from db import db

class Category(db.Model):
    '''categories table'''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))


    def __init__(self,name):
        self.name = name

    def json(self):
        return {'id':self.id, 'name' : self.name}

    @classmethod
    def find_by_id(cls,_id):
        '''Find Category by ID and return Category Instance'''
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        '''Save Category to database'''
        db.session.add(self)
        db.session.commit()

