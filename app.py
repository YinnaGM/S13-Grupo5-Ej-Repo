from os import name
from flask import Flask, request, render_template, redirect,url_for,session,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/ejemploflaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

# Creacion de Database a traves de las librerías
db = SQLAlchemy(app)

# Importar los modelos
from models import Admin, User, Profile, Type_food

# Crear el esquema de la DB
db.create_all()
db.session.commit()

#Rutas de página de inicio
@app.route('/')
def get_home():
 return render_template("home.html")

# Ruta del registro de usuario
@app.route('/register')
def register():
    return render_template("register.html")

# Ruta para crear el registro de usuario
@app.route('/create_user', methods=['POST'])
def create_user():

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        print(name)
        print(email)
        print(password)

        user = User(name,email,password)
        db.session.add(user)
        db.session.commit()

        found=User.query.filter(User.email==email)
        session['user_id'] = found[0].id
        print (session['user_id'])

        return render_template("profile.html")

# ruta para validar el usuario
@app.route('/check_user', methods=['POST'])
def check_user():
    email = request.form["email"]
    password = request.form["password"]

    if (email == "correo_Admin@gmail.com" and password =="admin"):
        return redirect (url_for('admin'))

    else:
        users=User.query.filter(User.password==password,User.email==email)

        try:
            if (users[0] is not None):
                session['user_id'] = users[0].id 
                print(session['user_id'] ) 
                return render_template("index.html") 
                
        except:
            print ("Email o Password incorrectos")
            flash("Email o Password incorrectos","alert-warning")
            return render_template('login.html')

# Ruta para el perfil de usuario
@app.route('/profile')
def profile():
    return render_template("profile.html")

# ruta para crear el perfil del usuario
@app.route('/create_profile', methods=['POST'])
def create_profile():

        sex = request.form["sex"]
        age = request.form["age"]
        height = request.form["height"]
        weight = request.form["weight"]
        insulin_type = request.form["insulin_type"]
        user_id = session['user_id']
        
        profile =Profile(sex, age, height, weight, insulin_type,user_id)
        
        db.session.add(profile)
        db.session.commit()   
        session.pop('user_id', None)
        return render_template("login.html")
 
# Ruta para ingresar el usuario
@app.route('/login')
def login():
  return render_template("login.html")
  
# ruta para el deslogueo del usuario
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return render_template("login.html")

# Ruta iniciada la sesion
@app.route('/index')
def index():
  return render_template("index.html")

# ruta para visualizar el perfil del usuario
@app.route('/view_profile')
def view_profile():
     return render_template("view_profile.html")


@app.route('/show_profile')    
def show_profile():
    consulta = Profile.query.all(Profile.user_id==session['user_id'])
    datos_perfil=Profile.query.all()
    
    print(session['user_id'])
    print(consulta.sex)
    print(datos_perfil)

    return "hola"
   
# Ruta para el calculo de insulina
@app.route('/Insulin_calculation')
def Insulin_calculation():
    return render_template("Insulin_calculation.html")

# ruta para alimentos
@app.route('/type_food')
def type_food():
  return render_template("type_food.html")

@app.route('/add_food',methods=['POST'])
def add_food():
    name = request.form["name"]
    category = request.form["category"] 
    quantity = request.form["quantity"]
    carbohydrate= request.form["carbohydrate"]

    type_food =Type_food( name,category,quantity,carbohydrate )
    db.session.add(type_food)
    db.session.commit() 
     
    session.pop('admin_id', None)
    return "Su registro se creo con exito"

#Rutas de ingreso administrador
@app.route('/admin')
def admin():
  return render_template("index_admin.html")

#Ruta para las transacciones del administrador
@app.route('/admin/transactions')
def admin_transactions():
  return render_template("crud_admin.html")

#Ruta para las Agregar nuevo administrador
@app.route('/crud_admin', methods=['GET','POST'])
def crud_admin():
        email =request.form['email']
        password = request.form['password']
        entry = Admin(email, password)
        db.session.add(entry)
        db.session.commit()
        flash("Se registro el admin exitosamente","alert-warning")
        return admin_transactions()

# Ruta para Actualizar nuevo administrador
@app.route('/updateadmin',methods=['GET','POST'])
def update_admin():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    old_admin = Admin.query.filter_by(email = old_email).first()
    old_admin.email = new_email
    db.session.commit()
    flash("Se actualizo el admin exitosamente","alert-warning")
    return admin_transactions()

@app.route('/getadmins')
def get_admins():
    admins = Admin.query.all()
    print(admins[0].email)
    return "Se trajo la lista de administradores registrados"

# Ruta para Eliminar administrador
@app.route('/deleteadmin',methods=['GET','POST'])
def delete_admin():
    admin_email = request.form['email']
    admin = Admin.query.filter_by(email = admin_email).first()
    print(admin_email)
    db.session.delete(admin)
    db.session.commit()
    flash("El Administrador se ha eliminado con exito","alert-warning")
    return admin_transactions()
