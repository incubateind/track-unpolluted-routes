from app import app,db
from flask import render_template,flash,redirect, url_for, request
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm, JourneyForm
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User, Record, Transport

@app.route('/')
@app.route('/base')
def base():
	return render_template('base.html')

@app.route('/index<id>')
@login_required
def index(id):
    
    return render_template('index2.html', current=id, name=User.query.get(id).username, gp1=User.query.get(id).green_points, gp2=Record.query.get(id).green_points)

@app.route('/journey<id>', methods=['GET','POST'])
def journey(id):
    
    form = JourneyForm()
    
    if form.validate_on_submit():
        transport = Transport.query.filter_by(dep=form.departure.data, arr=form.arrival.data).all()
        return render_template('journey.html', userid=id, name=User.query.get(id).username,\
        			gp1=User.query.get(id).green_points,\
        			gp2=Record.query.get(id).green_points,\
        			transports = transport, form=form)
    
    return render_template('journey.html', title='Register', form=form)

@app.route('/booked<int:uid>-<int:gp>', methods=['GET','POST'])
def booked(uid, gp):
    print(uid, gp)
    User.query.get(uid).green_points+=gp
    Record.query.get(uid).green_points+=gp
    db.session.commit()
    return render_template('transport.html', current=uid)

@app.route('/leaderboard<int:uid>', methods=['GET','POST'])
def leaderboard(uid):
	query=Record.query.order_by(Record.green_points.desc()).all()
	return render_template('leaderboard.html',query=query,id1=uid)


@app.route('/login', methods=['GET','POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('index', id=current_user.id))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user.id, user.username, user.email, user.green_points )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
    
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index', id=user.id)
        return redirect(next_page)
    
    #return render_template('index2.html',name=form.username.data, gp=user.green_points)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('base'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index',id=current_user.id))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, green_points=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        record = Record(green_points=0)
        db.session.add(record)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
