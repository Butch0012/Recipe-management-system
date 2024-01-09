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