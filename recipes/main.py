import click
from recipes.models import Recipe, session

@click.group()
def cli():
    """Main command group for the recipe management CLI."""
    pass