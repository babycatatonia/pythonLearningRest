from FlaskLearning.app import db

class BlogPostOrmModel(db.Model):
   id = db.Column(db.String(80) , primary_key=True)
   title = db.Column(db.String(80), nullable=False)
   text = db.Column(db.String(80), nullable=False)
   authorname = db.Column(db.String(80), nullable=False)