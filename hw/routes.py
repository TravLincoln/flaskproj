from hw import hw_obj
from flask import render_template, flash, redirect

from hw import db
from hw.models import User, Post
from hw.forms import CityForm

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
    people = {'Travis' : 25}
    title = 'My HomePage'
    topcities = ["Paris","London","Los Angeles","Tokyo"]
    posts = [{'author': 'john', 'body': 'Beautiful day in Portland!'},{'author': 'Susan', 'body': 'Today was a good day!'}]
    form = CityForm()
    if form.validate_on_submit():
        flash(f'City Chosen:  {form.cname.data}, rank={form.rank.data}')
        return redirect('/')
    return render_template("home.html",form=form, name=name, people=people, title=title,cities=topcities, posts=posts)

#@myapp_obj.route("/login", methods=['GET', 'POST'])
#def login():
   # form = LoginForm()
    #if form.validate_on_submit():
       # user = User.query.filter_by(username=form.username.data).first()
        #if user is None or not user.check_password(form.password.data):
           # flash('Login Invalid: Username or Password!')
            #return redirect('/login')
       # login_user(user, remember=form.remember_me.data)
       # flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
       # flash(f'Login password {form.password.data}')
       # return redirect('/')
   # return render_template("login.html", form=form)


#@myapp_obj.route("/members/<string:name>/")
#def getMember(name):
   # return 'Hi ' + name
