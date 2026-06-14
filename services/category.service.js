import recipes from "../data/seed.js";

export const getAllCategoriesService = () => {
  return [...new Set(recipes.map((r) => r.category))];
};

export const getByCategoryService = (category) => {
  return recipes.filter(
    (r) => r.category.toLowerCase() === category.toLowerCase()
  );
};