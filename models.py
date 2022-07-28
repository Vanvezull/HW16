from config import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    email = db.Column(db.String(120))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id" : self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(150))
    start_date = db.Column(db.Integer)
    end_date = db.Column(db.Integer)
    address = db.Column(db.String(120))
    prise = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    def to_dict(self):
        return {
            "id" : self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "prise": self.prise,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }

class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(f'{Order.__tablename__}.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(f'{User.__tablename__}.id'))

    def to_dict(self):
        return {
            "id" : self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }

