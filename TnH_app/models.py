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
