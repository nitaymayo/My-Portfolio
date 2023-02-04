from flask import Blueprint, render_template, request
from utilities.db.itemsManager import recipeHandler

# recipe blueprint definition
recipe = Blueprint('recipe',
                    __name__,
                    static_folder='static',
                    static_url_path='/recipe',
                    template_folder='templates')


# Routes
@recipe.route('/recipe')
def index():
    if request.args:
        recipe_id = request.args['recipe_id']
        recipe_info = recipeHandler.pullRecipe(recipe_id)
        recipe_steps = recipeHandler.pullRecipeSteps(recipe_id)
        recipe_ingredients = recipeHandler.pullRecipeIngredients(recipe_id)
        recipe_images = recipeHandler.pullRecipeImages(recipe_id)
        recipe = {
            'info': recipe_info[0],
            'steps': recipe_steps,
            'ingredients': recipe_ingredients,
            'images': recipe_images,
        }
        return render_template('recipe.html', recipe=recipe)
    return render_template('recipe.html')
