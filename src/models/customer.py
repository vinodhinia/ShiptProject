from db import db

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address = db.Column(db.String(100))

    orders = db.relationship('Order', lazy='dynamic')

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def json(self):
        return {'id':self.id, 'first_name' : self.first_name , 'last_name' : self.last_name, 'address' : self.address}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()





