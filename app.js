import express from "express";
import cors from "cors";

import searchRoutes from "./routes/search.routes.js";
import categoryRoutes from "./routes/category.routes.js";

import notFound from "./middleware/notFound.middleware.js";
import errorHandler from "./middleware/error.middleware.js";

const app = express();


app.use(
  cors({
    origin: ["http://localhost:5173", "http://localhost:5174"],
    methods: ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);

// JSON + form parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use("/api/search", searchRoutes);
app.use("/api/categories", categoryRoutes);


app.get("/", (req, res) => {
  res.json({
    success: true,
    message: "Recipe API is running"
  });
});


app.use(notFound);
app.use(errorHandler);

export default app;