from db import db

class Customer(db.Model):
    '''customers table'''
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address = db.Column(db.String(100))

    orders = db.relationship('Order', lazy='dynamic', back_populates = 'customer')

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def json(self):
        return {'id':self.id, 'first_name' : self.first_name , 'last_name' : self.last_name, 'address' : self.address}

    @classmethod
    def find_by_id(cls, _id):
        '''Find Customer by ID and return Customer Instance'''
        return cls.query.filter_by(id = _id).first()

    @classmethod
    def find_by_name(cls, name):
        '''Find Customer by name'''
        return cls.query.filter_by(name = name).first()


    def save_to_db(self):
        '''Save Customer to the Database'''
        db.session.add(self)
        db.session.commit()









