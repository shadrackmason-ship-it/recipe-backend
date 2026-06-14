export const connectDB = async () => {
  try {
    console.log(" Database not connected yet (using seed data)");
    // Later upgrade: MongoDB / PostgreSQL connection goes here
  } catch (error) {
    console.error(" DB connection error:", error);
  }
};