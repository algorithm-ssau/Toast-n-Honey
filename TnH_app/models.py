from . import db

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.NVARCHAR(100), nullable=False)
    Phone = db.Column(db.NVARCHAR(10), nullable=False)
    Email= db.Column(db.NVARCHAR(100))

    def __init__(self, Name, Phone, Email):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email

    def __repr__(self):
        return '<Customers %d: Name: %c, Phone: %c, Email: %c>' % (self.id, self.Name, self.Phone, self.Email) 

