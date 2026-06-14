import express from "express";
import {
  getRecipesByCategory,
  getAllCategories
} from "../controllers/category.controller.js";

const router = express.Router();

router.get("/", getAllCategories);

router.get("/:category", getRecipesByCategory);

export default router;