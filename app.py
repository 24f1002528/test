from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_restful import Api,Resource

from api import StudentAPI

api=None

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'


db.init_app(app)
api = Api(app)

class Course(db.Model):
    course_id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    course_name =db.Column(db.String,nullable=False)
    course_code=db.Column(db.String,unique=True,nullable=False)
    course_description = db.Column(db.String)	

class Student(db.Model):
    student_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    roll_number=db.Column(db.String,unique=True,nullable=False)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String)

class Enrollment(db.Model):
    enrollment_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    student_id=db.Column(db.Integer,db.ForeignKey(Student.student_id),nullable=False)
    course_id=db.Column(db.Integer,db.ForeignKey(Course.course_id),nullable=False)

@app.route('/')
def home():
    return 'Home page'

@app.route('/api/course/course_id',methods=['GET','POST'])
def get_course(course_id):
    course_detail = db.session.get(course_id)

    return render_template('course_details.html',course_detail=course_detail)

api.add_resource(StudentAPI,"/api/course/<string:course_id>","/api/course")

if __name__ =='__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()
