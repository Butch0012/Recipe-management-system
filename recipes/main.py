import click
from recipes.models import Recipe, session

@click.group()
def cli():
    """Main command group for the recipe management CLI."""
    pass

@cli.command()
@click.argument('name')
@click.argument('ingredients')
@click.argument('instructions')
def add(name, ingredients, instructions):
    """Add a new recipe."""
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
    session.add(new_recipe)
    session.commit()
    click.echo(f"Recipe '{name}' added successfully!")
    
@cli.command()
def view():
    """View all recipes."""
    # Query all recipes from the database
    recipes = session.query(Recipe).all()