from app import db
# Tabla Food
class Food(db.Model):
    __tablename__ = 'Food'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    grams = db.Column(db.Float)
    type_food_id = db.Column(db.ForeignKey("Type_food.id"))
    profile_id = db.Column(db.ForeignKey("Profile.id"))

    # Constructor
    def __init__(self, name, grams, type_food_id, profile_id):
        self.name = name
        self.grams = grams
        self.type_food_id = type_food_id
        self.profile_id = profile_id

# Tabla User
class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    
    # Constructor
    def __init__(self,name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Tabla Profile
class Profile(db.Model):
    __tablename__ = 'Profile'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    insulin_type = db.Column(db.String)
    user_id = db.Column(db.ForeignKey("User.id"))
    
    # Constructor
    def __init__(self, sex, age, height, weight, insulin_type,user_id):
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.insulin_type = insulin_type
        self.user_id = user_id

# Tabla Graph
class Graph(db.Model):
    __tablename__ = 'Graph'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    glycemia_user = db.Column(db.Float)
    fit_glycemia = db.Column(db.Float)
    date = db.Column(db.String)
    profile_id = db.Column(db.ForeignKey("Profile.id"))

    # Constructor
    def __init__(self, glycemia_user, fit_glycemia, date, profile_id):
        self.glycemia_user = glycemia_user
        self.fit_glycemia = fit_glycemia
        self.date = date
        self.profile_id = profile_id

# Tabla Type_food
class Type_food(db.Model):
    __tablename__ = 'Type_food'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    admin_id = db.Column(db.ForeignKey("Admin.id"))

    # Constructor
    def __init__(self, name, category, admin_id):
        self.name = name
        self.category = category
        self.admin_id = admin_id

# Tabla Admin
class Admin(db.Model):
    __tablename__ = 'Admin'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    # Constructor
    def __init__(self, email, password):
        self.email = email
        self.password = password

# Tabla Insulin_calculation
class Insulin_calculation(db.Model):
    __tablename__ = 'Insulin_calculation'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date = db.Column(db.String)
    profile_id = db.Column(db.ForeignKey("Profile.id"))
    food_id = db.Column(db.ForeignKey("Food.id"))

    # Constructor
    def __init__(self, date, profile_id, food_id):
        self.date = date
        self.profile_id = profile_id
        self.food_id = food_id

# Tabla History
class History(db.Model):
    __tablename__ = 'History'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    profile_id = db.Column(db.ForeignKey("Profile.id"))
    ins_calcul_id = db.Column(db.ForeignKey("Insulin_calculation.id"))

    # Constructor
    def __init__(self, profile_id, ins_calcul_id):
        self.profile_id = profile_id
        self.ins_calcul_id = ins_calcul_id

