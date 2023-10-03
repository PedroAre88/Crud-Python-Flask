from flask import Blueprint, render_template, request, redirect, url_for, flash
import mysql.connector

contacts = Blueprint('contacts', __name__, template_folder='app/templates')

#Coneccion a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flaskcrud",
    port='3306'
)

#Rutas para los metodos y consultas a la base de datos
@contacts.route('/')
def Index():
 cur = conn.cursor()
 cur.execute('SELECT * FROM contacts')
 data = cur.fetchall()
 conn.commit()
 return render_template('index.html', contacts = data)

@contacts.route('/add_contact', methods=['POST'])
def add_contact():
 if request.method == 'POST':
  fullname = request.form['fullname']
  phone = request.form['phone']
  email = request.form['email']
  cur = conn.cursor()
  cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
  conn.commit()
  flash('Contacto Agregado Satisfactoriamente!')
  
  return redirect(url_for('contacts.Index'))

@contacts.route('/edit/<id>')
def get_contact(id):
 cur = conn.cursor()
 cur.execute('SELECT * FROM contacts WHERE id = %s', (id,))
 data = cur.fetchall()
 conn.commit()
 return render_template('edit-contact.html', contact = data[0])

@contacts.route('/update/<id>', methods = ['POST'])
def update_contact(id):
  if request.method == 'POST':
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur = conn.cursor()
    cur.execute("""
   UPDATE contacts
   SET fullname = %s,
       email = %s,
       phone = %s
   WHERE id = %s 
""", (fullname, email, phone, id))
    conn.commit()
    flash('Contacto Actualizado Satisfactoriamente!')
    return redirect(url_for('contacts.Index'))

@contacts.route('/delete/<string:id>')
def delete_contact(id):
 cur = conn.cursor()
 cur.execute('DELETE FROM contacts WHERE id = %s', (id,))
 conn.commit()
 flash('Contacto Eliminado Satisfactoriamente!')
 return redirect(url_for('contacts.Index'))