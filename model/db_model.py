from create_app import db

class pois(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(45), nullable=False)
    ptype = db.Column(db.String(24), nullable=False)
    pclass = db.Column(db.String(30), nullable=False)
    plocation = db.Column(db.String(100), nullable=False)
    paddress = db.Column(db.String(100), nullable=False)
    pphoto = db.Column(db.JSON, nullable=True)
    pgrade = db.Column(db.String(45), nullable=True)
    plevel = db.Column(db.String(5), nullable=True)
    pprice = db.Column(db.String(300), nullable=True)
    pintroduce_long = db.Column(db.String(2400), nullable=True)
    pintroduce_short = db.Column(db.String(2400), nullable=True)
    popen_time = db.Column(db.String(300), nullable=True)
    pphonenumber = db.Column(db.String(100), nullable=True)
    precommended_duration = db.Column(db.String(50), nullable=True)
    prank = db.Column(db.String(4), nullable=True)



class TravelPlan(db.Model):
    tid = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(20), nullable=False)
    tuid = db.Column(db.Integer, nullable=False)
    tstart_day = db.Column(db.Date, nullable=True)
    tdays = db.Column(db.Integer, nullable=True)
    tday = db.Column(db.Integer, nullable=False)
    tpid = db.Column(db.Integer, nullable=False)
    tstart_time = db.Column(db.Time, nullable=True)
    tduration = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<TravelPlan {self.tid}>'
    


class Users(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    upassword = db.Column(db.String(20), nullable=False, default='000000')
    uname = db.Column(db.String(30))
    upic = db.Column(db.String(255))
    unickname = db.Column(db.String(20))
    
    

class Comments(db.Model):
    __tablename__ = 'comments'

    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cuid = db.Column(db.Integer, nullable=False)
    ctime = db.Column(db.Date, nullable=False)
    cgrade = db.Column(db.Float, nullable=True)
    ccontent = db.Column(db.String(2000), nullable=True)
    cpname = db.Column(db.String(45), nullable=True)
    cpid = db.Column(db.Integer, nullable=True)
    cphoto = db.Column(db.JSON, nullable=True)



class Event(db.Model):
    __tablename__ = 'event'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    point = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    rid = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)



class Record(db.Model):
    __tablename__ = 'record'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    point = db.Column(db.JSON, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    uid = db.Column(db.Integer, nullable=True)



class Plan(db.Model):
    __tablename__ = 'plan'  

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    itidata = db.Column(db.JSON, nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    pic = db.Column(db.String(255), nullable=False, default='https://d-hbing.huaban.com/661d35eca632861478a559fbd5fd02894b2223cc48-D4lkwtfw120webp')
    edittime = db.Column(db.String(31), nullable=True)