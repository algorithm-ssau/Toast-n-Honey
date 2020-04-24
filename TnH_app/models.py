from . import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    optionId = db.Column(db.Integer, db.ForeignKey('options.id'), nullable=False)

    def __init__(self, CustomerId, ProductId, OptionId):
        self.CustomerId = CustomerId
        self.ProductId = ProductId
        self.OptionId = OptionId

    def __repr__(self):
        return '<Order %d: CustomerID: %d, ProductID: %d, OptionID: %d>' % (self.OrderId, self.CustomerId, self.ProductId, self.OptionId)


class Options(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer)
    amount = db.Column(db.Integer)

    def __init__(self, ProductId, Price, Weight, Amount):
        self.ProductId = ProductId
        self.Price = Price
        self.Weight = Weight
        self.Amount = Amount

    def __repr__(self):
        return '<Option %d: ProductID: %d, Price: %d, Weight: %d, Amount: %d>' % (self.id, self.productId, self.price, self.weight, self.amount)

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
        return '<Customer %d: Name: %c, Phone: %c, Email: %c>' % (self.id, self.Name, self.Phone, self.Email)