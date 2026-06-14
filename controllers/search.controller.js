import { searchRecipesService } from "../services/search.service.js";
import ApiResponse from "../utils/ApiResponse.js";

export const searchRecipes = (req, res, next) => {
  try {
    const { q, ingredient } = req.query;

    const results = searchRecipesService({ q, ingredient });

    return res.json(
      new ApiResponse("Search successful", results)
    );
  } catch (err) {
    next(err);
  }
};