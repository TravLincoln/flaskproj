from hw import hw_obj
from flask import render_template, flash, redirect

from hw import db
from hw.models import User, Post
from hw.forms import TopCities

#@myapp_obj.route("/loggedin")
#@login_required
#def log():
    #return 'Hi! You are logged in'

#@myapp_obj.route("/logout")
#def logout():
   # logout_user()
    #return redirect('/')

@hw_obj.route("/", methods=['GET','POST'])
def hello():
    name = 'Travis'
    title = 'My HomePage'
    #topcities = ["Paris","London","Los Angeles","Tokyo"]
    form = TopCities()
    top_cities= User.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(cname=form.cname.data).first()
        u = User(cname=form.cname.data,rank=form.rank.data)
        db.session.add(u)
        db.session.commit()
        return redirect('/')
    return render_template("home.html",form=form,top_cities=top_cities, name=name, title=title)

#@myapp_obj.route("/login", methods=['GET', 'POST'])
#def login():
   # form = LoginForm()
   # if form.validate_on_submit():
        #user = User.query.filter_by(username=form.username.data).first()
    #    if user is None or not user.check_password(form.password.data):
     #       flash('Login Invalid: Username or Password!')
      #      return redirect('/login')
       # login_user(user, remember=form.remember_me.data)
        #flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        #flash(f'Login password {form.password.data}')
        #return redirect('/')
   # return render_template("login.html", form=form)


#@myapp_obj.route("/members/<string:name>/")
#def getMember(name):
   # return 'Hi ' + name
