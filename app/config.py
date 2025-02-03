# Global configuration settings (DB URL, API keys)
# Configuration settings for Safe Yatra
import os

# MongoDB connection URI (can be set via environment variable)
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/safe_yatra")

# Google Maps API Key (set via environment variable in production)
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "AIzaSyDf34ue6DB4ukLmPqY09YJsZ4FXW_vs98Y")

# JWT Secret Key for token generation (replace with secure value)
JWT_SECRET = os.getenv("JWT_SECRET", "my_very_strong_secret_2803")
# JWT Algorithm
JWT_ALGORITHM = "HS256"
# Token expiration time (e.g., 30 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30
