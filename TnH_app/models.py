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

    orders = db.relationship('orders', backref='options', lazy=True)

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
    Email = db.Column(db.NVARCHAR(100))

    orders = db.relationship('orders', backref='customers', lazy=True)

    def __init__(self, Name, Phone, Email):
        self.Name = Name
        self.Phone = Phone
        self.Email = Email

    def __repr__(self):
        return '<Customer %d: Name: %c, Phone: %c, Email: %c>' % (self.id, self.Name, self.Phone, self.Email)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeId = db.Column(db.Integer, db.ForeignKey('types.id'), nullable=False)
    name = db.Column(db.NVARCHAR(100), nullable=False)
    description = db.Column(db.NVARCHAR(500), nullable=True)
    photo = db.Column(db.NVARCHAR(100), nullable=True)

    options = db.relationship('options', backref='products', lazy=True)
    orders = db.relationship('orders', backref='products', lazy=True)

    def __init__(self, TypeId, Name, Description, Photo):
        self.TypeId = TypeId
        self.Name = Name
        self.Description = Description
        self.Photo = Photo

    def __repr__(self):
        return '<Product %d: TypeID: %d, Name: %c, Description: %c, Photo: %c>' % (self.id, self.typeId, self.name, self.description, self.photo)


class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.NVARCHAR(100), nullable=False)

    products = db.relationship('products', backref='types', lazy=True)

    def __init__(self, Title):
        self.Title = Title

    def __repr__(self):
        return '<Type %d: Title: %c>' % (self.id, self.title)
