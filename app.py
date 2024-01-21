import requests
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memes.db"
app.config["SECRET_KEY"] = "some-secret-key"
db = SQLAlchemy(app)


class Meme(db.Model):
    __tablename__ = "memes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    box_count = db.Column(db.Integer)
    captions = db.Column(db.Integer)

    def __repr__(self):
        return f"<Meme(id={self.id}, name={self.name}, url={self.url}, width={self.width}, height={self.height}, box_count={self.box_count}, captions={self.captions})>"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "width": self.width,
            "height": self.height,
            "box_count": self.box_count,
            "captions": self.captions,
        }


@app.route("/")
def index():
    """
    Return first 10 memes from the database
    """
    memes = Meme.query.paginate(page=1, per_page=10)
    return render_template("index.html", memes=memes, page=1)


@app.route("/load_data", methods=["GET"])
def data():
    """
    Load the data from the API and add it to the database
    """
    meme_api_url = "https://api.imgflip.com/get_memes"
    response = requests.get(meme_api_url)
    data = response.json()
    memes = data["data"]["memes"]
    for meme in memes:
        new_meme = Meme(
            name=meme["name"],
            url=meme["url"],
            width=meme["width"],
            height=meme["height"],
            box_count=meme["box_count"],
            captions=meme["captions"],
        )
        db.session.add(new_meme)
    db.session.commit()
    return jsonify(memes)


@app.route("/memes/<int:page>", methods=["GET"])
def memes(page):
    """
    Return the memes from the database with pagination
    """
    print(f"Current page: {page}")
    memes = Meme.query.paginate(page=page, per_page=10)
    return render_template("render_memes.html", memes=memes, page=page)


if __name__ == "__main__":
    # Only run this once to create the database
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, port=5000)
