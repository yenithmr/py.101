from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarea.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class tarea(db.Model):
   id = db.Column('tarea_id', db.Integer, primary_key = True)
   nombre = db.Column(db.String(100))
   codigo = db.Column(db.String(50))
   ejercicio = db.Column(db.String(200))
   descripcion = db.Column(db.String(300))

   def __init__(self, nombre, codigo, ejercicio, descripcion):
       self.nombre = nombre
       self.codigo = codigo
       self.ejercicio = ejercicio
       self.descripcion = descripcion

@app.route('/')
def show_all():
   return render_template('show_all.html', tarea = tarea.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['nombre'] or not request.form['codigo'] or not request.form['ejercicio']:
         flash('Please enter all the fields', 'error')
      else:
         tarea1 = tarea(request.form['nombre'], request.form['codigo'],request.form['ejercicio'], request.form['descripcion'])

         db.session.add(tarea1)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    name = request.form.get("oldname")
    tarea1 = tarea.query.filter_by(nombre=name).first()
    return render_template('update.html', result = tarea1, oldname = name)

@app.route("/update_record", methods=["POST"])
def update_record():
    name = request.form.get("oldname")
    tarea1 = tarea.query.filter_by(nombre=name).first()
    tarea1.nombre = request.form['nombre']
    tarea1.codigo = request.form['codigo']
    tarea1.ejercicio = request.form['ejercicio']
    tarea1.descripcion = request.form['descripcion']
    db.session.commit()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("oldname")
    tarea1 = tarea.query.filter_by(nombre=name).first()
    db.session.delete(tarea1)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
