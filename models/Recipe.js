class Recipe {
  constructor({ id, name, category, ingredients, instructions, prepTime }) {
    this.id = id;
    this.name = name;
    this.category = category;
    this.ingredients = ingredients;
    this.instructions = instructions;
    this.prepTime = prepTime;
  }
}

export default Recipe;