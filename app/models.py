from . import db
from . import login_manager
from werkzeug.security import generate_password_harsh,check_password_harsh
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(255))
    email=db.Column(db.String,unique = True,index=True)
    passhere=db.Column(db.string(255))
    
    @property
    def password(self):
        raise AttributeError("Sorry you can't read the passcode")
    
    @password.setter
    def password(self,password):
        self.passhere=generate_password_harsh(password)

    def verify_passwords(self,password):
        return check_password_harsh(self.passhere,password)

    def __ref__(self):
        return f'User {self.username}'