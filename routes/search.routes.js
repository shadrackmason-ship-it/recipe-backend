import express from "express";
import { searchRecipes } from "../controllers/search.controller.js";

const router = express.Router();

router.get("/", searchRecipes);

export default router;