from flask import Flask, render_template, jsonify, request
import processor 
import requests
from bs4 import BeautifulSoup
import sqlite3

import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "nikhil09"

#def create_users_table():
 #   con = sqlite3.connect('database.db')
  # cur.execute('''
   #       username TEXT UNIQUE NOT NULL,
    #        password TEXT NOT NULL
     #   )
    #''')
    #con.commit()
    #con.close()




#def register_user_to_db(username, password):
 #   con = sqlite3.connect('database.db')
  #  cur = con.cursor()
   # cur.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password))
    #con.commit()
    #con.close()


#def check_user(username, password):
 #   con = sqlite3.connect('database.db')
  #  cur = con.cursor()
   # cur.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))

    #result = cur.fetchone()
    #if result:
     #   return True
    #else:
     #   return False



#@app.route("/")
#def index():
 #   return render_template('login.html')


#@app.route('/register', methods=["POST", "GET"])
#def register():
 #   if request.method == 'POST':
  #      username = request.form['username']
   #     password = request.form['password']

    #   return redirect(url_for('index'))
   # else:
    #    return render_template('register.html')


#@app.route('/login', methods=["POST", "GET"])
#def login():
    #if request.method == 'POST':
     #   username = request.form['username']
      #  password = request.form['password']
       # if check_user(username, password):
        #    session['username'] = username

   #     return redirect(url_for('home'))
  #  else:
 #       return redirect(url_for('index'))


#@app.route('/home', methods=['POST', "GET"])
#def home():
    #if 'username' in session:
   #     return render_template('index.html')
  #  else:
 #       return "Username or Password is wrong!"


#@app.route('/logout')
#def logout():
    #   session.clear()
 #   return redirect(url_for('index'))


#if __name__ == '__main__':
 #   create_users_table()
 #   app.run(debug=True)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response": response })
 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='8888', debug=True)

#if __name__ == '__main__':
 #   create_users_table()
  #  app.run(debug=True)
