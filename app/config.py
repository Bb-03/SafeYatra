# Global configuration settings (DB URL, API keys)
# Configuration settings for Safe Yatra

# <<<<<<< HEAD
import os
import certifi
from pymongo import MongoClient

# MongoDB Connection URI (can be set via environment variable)
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://bhavyajain035:password1234@cluster0.qs1fe.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")

# Secure MongoDB Connection using certifi
client = MongoClient(MONGODB_URL, tlsCAFile=certifi.where())

# Define MongoDB Database and Collections
db = client["your_database_name"]  # Replace with actual database name
incidents_collection = db["incidents"]  # Collection for incidents
clustered_collection = db["clustered"]  # Collection for clustered data
# =======
# MongoDB connection URI (can be set via environment variable)
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://bhavyajain035:password1234@cluster0.qs1fe.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true")
# >>>>>>> 0b4e7df2a956d983964066f8188caa0a2bfb27cd

# Google Maps API Key (set via environment variable in production)
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Twilio Configuration
TWILIO_SID = os.getenv("TWILIO_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "")

# JWT Secret Key for token generation (replace with secure value)
JWT_SECRET = os.getenv("JWT_SECRET", "my_very_strong_secret_2803")

# JWT Algorithm
JWT_ALGORITHM = "HS256"

# Token expiration time (e.g., 30 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30



