import os

class Config:
    # Required for sessions/authentication
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(24).hex()
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'sqlite:///bookdb.sqlite'  # Fallback for development
    )
    
    # Disable modification tracking for better performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False