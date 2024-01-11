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
     # Check if there are no recipes
    if not recipes:
        click.echo("No recipes available.")
    else:
        # Display each recipe's ID and name
        for recipe in recipes:
            click.echo(f"{recipe.id}. {recipe.name}")
@cli.command()
@click.argument('recipe_id', type=int)
def update(recipe_id):
    """Update a recipe."""
    # Add logic to update a specific recipe based on the recipe_id
    pass
@cli.command()
@click.argument('recipe_id', type=int)
def delete(recipe_id):
    """Delete a recipe."""
    # Add logic to delete a specific recipe based on the recipe_id
    pass
@cli.command()
@click.argument('ingredient')
def search_by_ingredient(ingredient):
    """Search recipes by ingredient."""
    # Add logic to query and display recipes containing the specified ingredient
    pass
            

if __name__ == '__main__':
 cli()