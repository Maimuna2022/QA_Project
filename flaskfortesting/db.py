from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    recipes = db.relationship('Recipe', backref='all_recipes')


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String)
    recipe_instructions = db.Column(db.String)
    type_of_dish = db.Column(db.String)
    origin = db.Column(db.String)
    users = db.Column(db.ForeignKey('recipe.user_id'))

db.create_all()
u1 = User(id=1, first_name='Elizabeth', last_name='Charles', email='e.charles@gmail.com')
u2 = User(id=2, first_name='Susan', last_name='smith', email='s.smith@gmail.com')
u3 = User(id=3, first_name='Mellisa', last_name='gallaway', email='m.gallaway@gmail.com')
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.commit()
r1 = Recipe(id=1, recipe_name='Naan bread', type_of_dish='side', origin='Ancient Egypt and South Asia', recipe_instructions='Combine warm water, yeast, and sugar in a large bowl; let sit for five minutes or till bubbly. Add olive oil, yogurt, egg, salt, and 2 cups of flour. Stir till smooth.'
                                                                'Add enough flour to make a soft dough. Knead a few times on a floured counter until smooth. '
                                                                'Place dough in a greased bowl. Cover and let rise in a warm place until doubled.'
                                                                'Preheat a skillet to medium heat.'
                                                                'Cut dough into eight pieces. On a floured surface, roll out each piece into a 6" circle. '
                                                                'Add a little oil or non-stick spray to the skillet. Cook each circle for 2-3 minutes or until bubbly and golden brown on the bottom. Flip over and cook for another 2-3 minutes.'
                                                                'Brush the top (the bubbly side) of each naan with melted butter. I added garlic to my butter, but that is optional.')
r2 = Recipe(id=2, recipe_name='crepe', type_of_dish='breakfast', origin='France', recipe_instructions='In a large mixing bowl, whisk together the flour and the eggs. Gradually add in the milk and water, stirring to combine. Add the salt and butter; beat until smooth.'
                                                                                                      'Heat a lightly oiled griddle or frying pan over medium high heat. Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each crepe. Tilt the pan with a circular motion so that the batter coats the surface evenly.'
                                                                                                      'Cook the crepe for about 2 minutes, until the bottom is light brown. Loosen with a spatula, turn and cook the other side. Serve hot.')
db.session.add(r1)
db.session.add(r2)
db.session.commit()
