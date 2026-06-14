import recipes from "../data/seed.js";

export const searchRecipesService = ({ q, ingredient }) => {
  let results = recipes;

  if (q) {
    results = results.filter(r =>
      r.name.toLowerCase().includes(q.toLowerCase())
    );
  }

  if (ingredient) {
    results = results.filter(r =>
      r.ingredients.includes(ingredient.toLowerCase())
    );
  }

  return results;
};