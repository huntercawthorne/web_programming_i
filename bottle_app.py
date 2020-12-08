import datetime
import time
<<<<<<< HEAD
import os
import random
import sqlite3
import uuid

from tinydb import TinyDB, Query
db = TinyDB("sessions.json")
query = Query()

from bottle import get, post, request, response, template, redirect
=======
import uuid
import dataset

db = dataset.connect('sqlite:///todo.db')
>>>>>>> 21696687a61c2083725d5abb03db46140a5e20f5

from bottle import get, post, request, response, template, redirect, default_app

<<<<<<< HEAD
if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import run, debug
=======
def get_session(request, response):
    session_id = request.cookies.get("session_id",None)
    if session_id == None:
        session_id = str(uuid.uuid4())
        session = { 'session_id':session_id, "username":"Guest", "time":int(time.time()) }
        db['session'].insert(session)
        response.set_cookie("session_id",session_id)
    else:
        session=db['session'].find_one(session_id=session_id)
        if session == None:
            session_id = str(uuid.uuid4())
            session = { 'session_id':session_id, "username":"Guest", "time":int(time.time()) }
            db['session'].insert(session)
            response.set_cookie("session_id",session_id)

            # session = {"message":"no session found with the id =" + session_id}
    return session

def save_session(session):
    db['session'].update(session,['session_id'])

@get('/login')
def get_login():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    return template("login", csrf_token="abcrsrerredadfa")

@post('/login')
def post_login():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    # csrf_token = request.forms.get("csrf_token").strip()
    # if csrf_token != "abcrsrerredadfa":
    #     redirect('/login_error')
    #     return
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    profile = db['profile'].find_one(username=username)
    if profile == None:
        redirect('/login_error')
        return
    if password != profile["password"]:
        redirect('/login_error')
        return
    session['username'] = username
    save_session(session)
    redirect('/')


@get('/logout')
def get_logout():
    session = get_session(request, response)
    session['username'] = 'Guest'
    save_session(session)
    redirect('/login')

@get('/register')
def get_register():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    return template("register", csrf_token="abcrsrerredadfa")

@post('/register')
def post_register():
    session = get_session(request, response)
    if session['username'] != 'Guest':
        redirect('/')
        return
    # csrf_token = request.forms.get("csrf_token").strip()
    # if csrf_token != "abcrsrerredadfa":
    #     redirect('/login_error')
    #     return
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    if len(password) < 8:
        redirect('/login_error')
        return
    profile = db['profile'].find_one(username=username)
    if profile:
        redirect('/login_error')
        return
    db['profile'].insert({'username':username, 'password':password})
    redirect('/')
>>>>>>> 21696687a61c2083725d5abb03db46140a5e20f5

random.seed()

@get('/')
def get_show_list():
<<<<<<< HEAD

    # ask for cookie, if we don't have one start a guest session
    session_id = request.cookies.get("session_id",None)
    if session_id == None:
        session_id = str(uuid.uuid4())
        session = {'session_id':session_id, "username":"Guest", "time":int(time.time())}
        db.insert(session)
        response.set_cookie("session_id",session_id)
    # had a cookie with an id, look up the session
    else:
        result = db.search(query.session_id == session_id)
        # the session isn't found, start a new one
        if len(result) == 0:
            session_id = str(uuid.uuid4())
            session = {'session_id':session_id, "username":"Guest", "time":int(time.time())}
            db.insert(session)
            response.set_cookie("session_id",session_id)
        # the session is found, use it
        else:
            session=result[0]

    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result, session={})

@get('/sandbox')
def get_sandbox():
    return template("sandbox")

@get('/ajaxdemo')
def get_ajaxdemo():
    return template("ajaxdemo")

@get('/jquerydemo')
def get_jquerydemo():
    return template("jquerydemo")

@get('/login')
def get_login():
    return template("login", csrf_token="abcrsrerredadfa")

@post('/login')
def post_login():
    csrf_token = request.forms.get("csrf_token").strip()
    if csrf_token != "abcrsrerredadfa":
        redirect('/login_error')
        return
    username = request.forms.get("username").strip()
    password = request.forms.get("password").strip()
    if password != "password":
        redirect('/login_error')
        return
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'username':username})
    else:
        session = result[0]
        db.update({'username':username},query.session_id == session_id)
    response.set_cookie("session_id",session_id)
    redirect('/')

@get('/logout')
def get_logout():
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'username':"Unknown"})
    else:
        db.update({'username':"Unknown"},query.session_id == session_id)
    response.set_cookie("session_id",session_id)
    redirect('/')

@get('/login_error')
def get_login_error():
    return template("login_error")

@get('/set_status/<id:int>/<value:int>')
def get_set_status(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status=? where id=?", (value, id,))
    connection.commit()
    cursor.close()
=======
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    result = db['todo'].all()
    result=[dict(r) for r in result]
    return template("show_list", rows=result, session=session)


@get('/update_status/<id:int>/<value:int>')
def get_update_status(id, value):
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    #result = db['todo'].find_one(id=id)
    db['todo'].update({'id':id, 'status':(value!=0)},['id'])
    redirect('/')


@get('/delete_item/<id:int>')
def get_delete_item(id):
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    db['todo'].delete(id=id)
    redirect('/')


@get('/update_task/<id:int>')
def get_update_task(id):
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    result = db['todo'].find_one(id=id)
    return template("update_task", row=result)


@post('/update_task')
def post_update_task():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    id = int(request.forms.get("id").strip())
    updated_task = request.forms.get("updated_task").strip()
    db['todo'].update({'id':id, 'task':updated_task},['id'])
>>>>>>> 21696687a61c2083725d5abb03db46140a5e20f5
    redirect('/')


@get('/new_item')
def get_new_item():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    return template("new_item")


@post('/new_item')
def post_new_item():
    session = get_session(request, response)
    if session['username'] == 'Guest':
        redirect('/login')
        return
    new_task = request.forms.get("new_task").strip()
    db['todo'].insert({'task':new_task, 'status':False})
    redirect('/')

<<<<<<< HEAD

@get('/update_item/<id:int>')
def get_update_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result[0])


@post('/update_item')
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set task=? where id=?", (updated_item, id,))
    connection.commit()
    cursor.close()
    redirect('/')

@get('/delete_item/<id:int>')
def get_delete_item(id):
    print("we want to delete #" + str(id))
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    connection.commit()
    cursor.close()
    redirect('/')

@get("/picture")
def get_picture():
    # picture from here: https://editor.p5js.org/p5/sketches/Hello_P5:_animate
    # p5js.org
    return template("picture")


@get("/visit")
def get_visit():
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'visit_count':1})
        visit_count = 1
    else:
        session = result[0]
        visit_count = session['visit_count'] + 1
        db.update({'visit_count':visit_count},query.session_id == session_id)
    response.set_cookie("session_id",session_id)
    return(f"Welcome, session_id #{session_id}. Visit# {visit_count}.")

if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=8080)

=======

application = default_app()


if __name__ == "__main__":
    #print(get_show_list())
    get_update_task(6)
>>>>>>> 21696687a61c2083725d5abb03db46140a5e20f5
