from utilities.db.db_manager import dbManager


class ItemsManager:
    def getTable(self, var):
        return dbManager.fetch("select * from %s" % (var))

    def getTableByLimit(self, var, offset, rows_num):
        res = dbManager.fetch("select * from %s limit %s, %s" % (var, offset, rows_num))
        return res

class ArticleHandler:
    def pullArticle(self, art_id):
        query_res = dbManager.fetch('SELECT * FROM articles WHERE Article_ID = %s', (art_id,))
        return query_res

class ProductHandler:
    def pullProduct(self, product_id):
        query_res = dbManager.fetch("SELECT * FROM products WHERE Product_ID = %s", (product_id,))
        return query_res

class RecipeHandler:
    def pullRecipe(self, recipe_id):
        recipe_info = dbManager.fetch("SELECT * FROM recipes WHERE Recipe_ID = %s", (recipe_id,))
        return recipe_info

    def pullRecipeSteps(self, recipe_id):
        recipe_steps = dbManager.fetch("SELECT * FROM recipe_steps WHERE Recipe_ID = %s order by step_num asc", (recipe_id,))
        return recipe_steps

    def pullRecipeIngredients(self, recipe_id):
        recipe_ingredients = dbManager.fetch("SELECT * FROM recipe_ingredients WHERE Recipe_ID = %s", (recipe_id,))
        return recipe_ingredients

    def pullRecipeImages(self, recipe_id):
        recipe_images = dbManager.fetch("SELECT * FROM recipe_photos WHERE Recipe_ID = %s", (recipe_id,))
        return recipe_images


# Creates an instance for the DBManager class for export.
itemsManager = ItemsManager()

recipeHandler = RecipeHandler()

productHandler = ProductHandler()

articleHandler = ArticleHandler()