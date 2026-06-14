import recipes from "../data/recipes.js";

export const searchRecipes = (req, res) => {
  const { query, category } = req.query;

  let results = recipes;

  if (query) {
    const q = query.toLowerCase();

    results = results.filter((r) =>
      r.name.toLowerCase().includes(q) ||
      r.ingredients.some((i) => i.toLowerCase().includes(q))
    );
  }

  if (category && category !== "All") {
    results = results.filter((r) => r.category === category);
  }

  res.json({
    success: true,
    data: results,
  });
};