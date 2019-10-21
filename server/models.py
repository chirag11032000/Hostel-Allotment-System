from server import db

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key = True)
    roll_number = db.Column(db.Integer, unique = True)
    name = db.Column(db.String(20))
    email_id = db.Column(db.String(20), unique = True)
    phone_number = db.Column(db.Integer)
    cgpi = db.Column(db.Float)
    year = db.Column(db.Integer)
    password = db.Column(db.Text)


class Admin(db.Model):
    __tablename__ = "admins"
    user_name = db.Column(db.String(20), primary_key = True)
    password = db.Column(db.Text)


class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    size = db.Column(db.Integer)
    is_lock = db.Column(db.Boolean)


class Member(db.Model):
    __tablename__ = "member"
    student_id = db.Column(db.Integer, db.ForeignKey("Student.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("Team.id"))


class Room(db.Model):
    __tablename__ = "rooms"
    room_no = db.Column(db.Integer)
    location_x = db.Column(db.Integer)
    location_y = db.Column(db.Integer)
    location_z = db.Column(db.Integer)
    is_allocated = db.Column(db.Boolean)
    room_capacity = db.Column(db.Integer)


class Round(db.Model):
    __tablename__ = "rounds"
   round_no = db.Column(db.Integer)
   start_time = db.Column(db.DateTime)
   duration = db.Column(db.Integer)


class Choice(db.Model):
    __tablename__ = "choices"
    team_id = db.Column(db.Integer, db.ForeignKey("Team.id"))
    choice_no = db.Column(db.Integer)
    room_no = db.Column(db.Integer, db.ForeignKey("Room.room_no"))
