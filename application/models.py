from application import db, app

app.app_context().push();

class FriendsCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    catch_phrase = db.Column(db.String(100), nullable=False)

    def __init__(self, name, age, catch_phrase):
        self.name = name
        self.age = age
        self.catch_phrase = catch_phrase