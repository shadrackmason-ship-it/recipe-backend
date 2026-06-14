import {
  getByCategoryService,
  getAllCategoriesService,
} from "../services/category.service.js";

import ApiResponse from "../utils/ApiResponse.js";


export const getAllCategories = (req, res, next) => {
  try {
    const categories = getAllCategoriesService();

    return res.json(
      new ApiResponse("Categories fetched successfully", categories)
    );
  } catch (err) {
    next(err);
  }
};


export const getRecipesByCategory = (req, res, next) => {
  try {
    const { category } = req.params;

    const results = getByCategoryService(category);

    return res.json(
      new ApiResponse("Category fetch successful", results)
    );
  } catch (err) {
    next(err);
  }
};