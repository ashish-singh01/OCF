from flask import Flask,request
import bcrypt
from flask_smorest import Api, abort
from database import USER,PASSWORD
from flask_sqlalchemy import SQLAlchemy
import uuid
#from users import UserModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USER}:{PASSWORD}@{'localhost'}/{'users'}"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)

# conn = sqlite3.connect('users')
# cursor = conn.cursor()

#cursor.execute("CREATE TABLE userInfo (name VARCHAR(80),email VARCHAR(80), passwd VARCHAR(100), id int PRIMARY_KEY )")

#creating userInfo table model
class UserModel(db.Model):
    __tablename__ = 'userInfo'

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    passwd = db.Column(db.String(80), nullable=False)

    # def __init__(self, id, name, email, passwd):
    #     id=self.id
    #     name=self.name
    #     email=self.email
    #     passwd=self.passwd




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
    salt = bcrypt.gensalt()
    if UserModel.query.filter(UserModel.email == request.form.get('email')).first():
        return 'User already exists', 409

    byte = (request.form.get('passwd')).encode('utf-8')
    details = UserModel(
        id = (uuid.uuid4()),
        name = request.form.get('name'),
        email = request.form.get('email'),
        passwd = bcrypt.hashpw(byte,salt)
    )
    #print(details.passwd)
    db.session.add(details)
    db.session.commit()
    return 'User registered', 200
    

if __name__ == '__main__':
    create_db()
    api = Api(app)
    api.register_blueprint(UserModel)
    app.run(debug=True)
    