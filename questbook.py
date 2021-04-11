from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'123abc'

db = SQLAlchemy(app)

class Guestbook(db.Model):  # 留言板資料表
    id = db.Column(db.Integer, primary_key=True)
    guestname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(10), nullable=False,
        default='ico1.png')
    postdate = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return 'guestname:{},email:{},postdate:{}'.format(
            self.guestname,
            self.email,
            self.postdate
        )

class User(UserMixin, db.Model):  # 使用者資料表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    pwd_hash = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def verify_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    @property
    def password(self):
        raise AttributeError('無法讀取password屬性')

    @password.setter
    def password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def __repr__(self):
        return f'name:{self.name},email:{self.email}'


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

# if __name__ == "__main__":
#     app.run('0.0.0.0', 80, debug=True)