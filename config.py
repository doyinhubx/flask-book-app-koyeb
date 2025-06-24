# # Original
# #--------------------------------------------------------------
# import os

# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_bookdb'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# Docker With local MySQL by connecting to host.docker.internal
#--------------------------------------------------------------
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'mysql://root:@host.docker.internal/flask_bookdb'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# # With Docker Compose file to spin up both MySQL + Flask together
# #--------------------------------------------------------------
# import os

# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')
#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         'SQLALCHEMY_DATABASE_URI',
#         'mysql://root:@localhost/flask_bookdb'
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


