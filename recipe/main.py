# main.py
import click
from models import Base, engine
from sqlalchemy.orm import sessionmaker
from recipe_model import Recipe

# Create tables if not exist
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

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
    recipes = session.query(Recipe).all()
    if not recipes:
        click.echo("No recipes available.")
    else:
        for recipe in recipes:
            click.echo(f"{recipe.id}. {recipe.name}")

@cli.command()
@click.argument('recipe_id', type=int)
@click.argument('new_name')
@click.argument('new_ingredients')
@click.argument('new_instructions')
def update(recipe_id, new_name, new_ingredients, new_instructions):
    """Update a recipe."""
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        click.echo(f"No recipe found with ID {recipe_id}.")
        return

    recipe.name = new_name
    recipe.ingredients = new_ingredients
    recipe.instructions = new_instructions
    session.commit()
    click.echo(f"Recipe with ID {recipe_id} updated successfully.")

@cli.command()
@click.argument('recipe_id', type=int)
def delete(recipe_id):
    """Delete a recipe."""
    recipe = session.query(Recipe).filter_by(id=recipe_id).first()
    if not recipe:
        click.echo(f"No recipe found with ID {recipe_id}.")
        return

    session.delete(recipe)
    session.commit()
    click.echo(f"Recipe with ID {recipe_id} deleted successfully.")

@cli.command()
@click.argument('ingredient')
def search_by_ingredient(ingredient):
    """Search recipes by ingredient."""
    recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f"%{ingredient}%")).all()
    if not recipes:
        click.echo(f"No recipes found containing '{ingredient}'.")
    else:
        click.echo(f"Recipes containing '{ingredient}':")
        for recipe in recipes:
            click.echo(f"{recipe.id}. {recipe.name}")

if __name__ == '__main__':
    cli()
