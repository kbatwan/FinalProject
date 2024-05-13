# import hashlib
# import flask
# from flask import jsonify
# from flask import request #, make_response

# import mysql.connector
# import creds
# from mysql.connector import Error
# from sql import create_connection
# from sql import execute_query
# from sql import execute_read_query


import flask
from flask import jsonify
from flask import request
import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#setting up an application name
app = flask.Flask(__name__)
app.config["DEBUG"] = True #allow to show errors in browser

#connection to mysql database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

@app.route('/', methods=['GET'])
def home():
    return "<h1> Day Care Facility Database Project </h1>"

#get all from table facility
@app.route('/api/facilities/all', methods=['GET'])
def api_facilities_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql ="Select * From facility" #sql Query
    facility = execute_read_query(conn, sql)
    return jsonify(facility)

#add a facility with POST method
@app.route('/api/facilities', methods=['POST'])
def api_add_facility():
    request_data = request.get_json()
    newfacility = request_data['name']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

    sqlQuery = "INSERT INTO facility (name) SELECT '%s' WHERE NOT EXISTS (SELECT 1 FROM facility WHERE name='%s')" % (newfacility, newfacility)
    execute_query(conn, sqlQuery)
    return "Completed"

# Delete facility with DELETE method
@app.route('/api/facilities_delete', methods=['DELETE'])
def api_delete_facility_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "Delete from facility where id = %s" % (id)
    execute_query(conn, sql)
        
    return "Delete request successful!"

# Update facility of specific id with PUT method
@app.route('/api/facilities_update', methods=['PUT'])
def api_update_facility_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    name = requested_data['name']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "update facility set name = '%s' where id = %s" % (name,id) 
    execute_query(conn, sql)
        
    return "Update request successful!"

#get all from table teacher
@app.route('/api/teachers/all', methods=['GET'])
def api_teachers_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql ="Select * From teacher" #sql Query
    teacher = execute_read_query(conn, sql)
    return jsonify(teacher)

#add a teacher with POST method
@app.route('/api/teachers', methods=['POST'])
def api_add_teacher():
    request_data = request.get_json()
    newteacherFname = request_data['firstname']
    newteacherLname = request_data['lastname']
    newteacherAge = request_data['age']
    newteacherRoom = request_data['room']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

    sqlQuery = "INSERT INTO teacher (firstname, lastname, age, room) SELECT '%s','%s',%s,%s WHERE NOT EXISTS (SELECT 1 FROM teacher WHERE firstname='%s' AND lastname='%s' AND age=%s AND room=%s)" % (newteacherFname,newteacherLname,newteacherAge,newteacherRoom,newteacherFname,newteacherLname,newteacherAge,newteacherRoom)
    execute_query(conn, sqlQuery)
    return "Completed"

# Delete teacher with DELETE method
@app.route('/api/teachers_delete', methods=['DELETE'])
def api_delete_teacher_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "Delete from teacher where id = %s" % (id)
    execute_query(conn, sql)
        
    return "Delete request successful!"

# Update teacher of specific id with PUT method
@app.route('/api/teachers_update', methods=['PUT'])
def api_update_teacher_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    firstname = requested_data['firstname']
    lastname = requested_data['lastname']
    age = requested_data['age']
    room = requested_data['room']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "update teacher set firstname = '%s', lastname = '%s', age = %s, room = %s where id = %s" % (firstname,lastname,age,room,id) 
    execute_query(conn, sql)
        
    return "Update request successful!"

#get all from table classroom
@app.route('/api/classrooms/all', methods=['GET'])
def api_classrooms_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql ="Select * From classroom" #sql Query
    classroom = execute_read_query(conn, sql)
    return jsonify(classroom)

#add a classroom with POST method
@app.route('/api/classrooms', methods=['POST'])
def api_add_classrooms():
    request_data = request.get_json()
    newclassCapacity = request_data['capacity']
    newclassName = request_data['name']
    newclassfacility = request_data['facility']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

    sqlQuery = "INSERT INTO classroom (capacity,name,facility) SELECT %s,'%s',%s WHERE NOT EXISTS (SELECT 1 FROM classroom WHERE capacity=%s AND name='%s' AND facility=%s)" % (newclassCapacity,newclassName,newclassfacility,newclassCapacity,newclassName,newclassfacility)
    execute_query(conn, sqlQuery)
    return "Completed"

# Delete classroom with DELETE method
@app.route('/api/classrooms_delete', methods=['DELETE'])
def api_delete_classrooms_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "Delete from classroom where id = %s" % (id)
    execute_query(conn, sql)
        
    return "Delete request successful!"

# Update classroom of specific id with PUT method
@app.route('/api/classrooms_update', methods=['PUT'])
def api_update_classrooms_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    capacity = requested_data['capacity']
    name = requested_data['name']
    facility = requested_data['facility']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "update classroom set capacity = %s, name = '%s', facility = %s where id = %s" % (capacity,name,facility,id) 
    execute_query(conn, sql)
        
    return "Update request successful!"

#get all from table child
@app.route('/api/child/all', methods=['GET'])
def api_child_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql ="Select * From child" #sql Query
    child = execute_read_query(conn, sql)
    return jsonify(child)

#add a child with POST method
@app.route('/api/child', methods=['POST'])
def api_add_child():
    request_data = request.get_json()
    newchildFname = request_data['firstname']
    newchildLname = request_data['lastname']
    newchildAge = request_data['age']
    newchildRoom = request_data['room']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

    sql1 ="Select COUNT(id) From teacher WHERE room = %s" % (newchildRoom)
    sql1answer = execute_read_query(conn, sql1)
    sql2 ="Select capacity From classroom WHERE id = %s" % (newchildRoom)
    sql2answer = execute_read_query(conn, sql2)
    sql1answers = sql1answer[0]['COUNT(id)']
    sql2answers = sql2answer[0]['capacity']
    teacher_capacity = sql1answers*10
    working_capacity = min(teacher_capacity,sql2answers)
    sql3 ="Select COUNT(id) From child WHERE room = %s" % (newchildRoom)
    sql3answer = execute_read_query(conn, sql3)
    sql3answers = sql3answer[0]['COUNT(id)']
    if sql3answers>=working_capacity:
        return "Cannot add this child to this classroom as it is at capacity "
    else:
        myCreds = creds.Creds()
        conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
        enrollment = sql3answers + 1
    sqlQuery = "INSERT INTO child (firstname, lastname, age, room) SELECT '%s','%s',%s,%s WHERE NOT EXISTS (SELECT 1 FROM teacher WHERE firstname='%s' AND lastname='%s' AND age=%s AND room=%s)" % (newchildFname,newchildLname,newchildAge,newchildRoom,newchildFname,newchildLname,newchildAge,newchildRoom)
    execute_query(conn, sqlQuery)
    return "Completed. The room now has %s children" % (enrollment)

# Delete child with DELETE method
@app.route('/api/child_delete', methods=['DELETE'])
def api_delete_child_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "Delete from child where id = %s" % (id)
    execute_query(conn, sql)
        
    return "Delete request successful!"

# Update child of specific id with PUT method
@app.route('/api/child_update', methods=['PUT'])
def api_update_child_byID():
    requested_data = request.get_json()
    id = requested_data['id']
    firstname = requested_data['firstname']
    lastname = requested_data['lastname']
    age = requested_data['age']
    room = requested_data['room']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "update child set firstname = '%s', lastname = '%s', age = %s, room = %s where id = %s" % (firstname,lastname,age,room,id) 
    execute_query(conn, sql)
        
    return "Update request successful!"


#Pre-configured User username and password for Login
authorizedUserAccount = [
    {
        # user
        'username': 'manager',
        'password': 'managerpassword',
        'userinfo': 'You are logged in!'
    }
]

#Login Api
# password is 'password' hashed
# masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
# masterUsername = 'username'

# @app.route('/authenticatedroute', methods=['GET'])
# def auth_example():
#     if request.authorization:
#         encoded = request.authorization.password.encode() #unicode encoding
#         hashedResult = hashlib.sha256(encoded) #hashing
#         if request.authorization.username == masterUsername and hashedResult.hexdigest() == masterPassword:
#             return '<h1> We are allowed to be here </h1>'
#     return make_response('COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/api/userlogin', methods=['POST'])
def auth_Usercredentials():
    json_data = request.get_json()
    username = json_data.username #header parameter
    password = json_data.password

    for user in authorizedUserAccount:
        if user['username'] == username and user['password'] == password :  #if the authorized user is found return their info
            userinfo = user['userinfo']
            results = []
            results.append(userinfo)
            return 'You are logged in!'
    return 'Incorrect Credentials!'

app.run(debug=True,use_reloader=False)