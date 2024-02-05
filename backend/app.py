from flask import Flask,request, jsonify
from flask_cors import CORS
import bcrypt
from flask_smorest import Api, abort
from database import USER,PASSWORD
from flask_sqlalchemy import SQLAlchemy
import uuid
#from users import UserModel

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{'localhost'}/{'users'}"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#creating userInfo table model
class UserModel(db.Model):
    __tablename__ = 'userInfo'

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    passwd = db.Column(db.String(80), nullable=False)




def create_db():
    with app.app_context():
        db.create_all()

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'../resources_test/upload/{file.filename}')
    return 'File Uploaded', 200

@app.route("/register", methods=['POST'])
def register():
    # userData = (request.form.items())
    #print(request.form.get('name'))
    #salt = bcrypt.gensalt()
    if UserModel.query.filter(UserModel.email == request.form.get('email')).first():
        return 'User already exists', 409

    #byte = (request.form.get('passwd')).encode('utf-8')
    details = UserModel(
        id = (uuid.uuid4()),
        name = request.form.get('name'),
        email = request.form.get('email'),
        passwd = bcrypt.hashpw((request.form.get('passwd')).encode('utf-8') , bcrypt.gensalt())
    )
    #print(details.passwd)
    db.session.add(details)
    db.session.commit()
    return 'successful', 200


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('passwd').encode('utf-8')
    user = UserModel.query.filter_by(email=email).first()
    #print(user.passwd)
    if bcrypt.checkpw(password, user.passwd.encode('utf-8')):
        # print(jsonify(user.name))
        data={'message': user.name }
        return jsonify(data), 200
    return "Password didn't match", 400


if __name__ == '__main__':
    create_db()
    api = Api(app)
    api.register_blueprint(UserModel)
    app.run(debug=True)



# username= test
# email= test@test.com   
# password = test