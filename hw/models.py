from hw import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(64), unique=False, index=True)
    rank = db.Column(db.Integer, unique=False)
    posts = db.relationship('Post', backref='author', lazy = 'dynamic')

    def __repr__(self):
        return f'{self.cname}, Rank:{self.rank}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'

