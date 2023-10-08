from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from super_admin_1.config import App_Config


db = SQLAlchemy()




def create_app():
    """
    Create a new instance of the app with the given configuration.

    :param config_class: configuration class
    :return: app
    """
    # Initialize Flask-

    app = Flask(__name__)
    app.config.from_object(App_Config)
    if app.config["SQLALCHEMY_DATABASE_URI"]:
        print(f"using db")

    # Initialize CORS
    CORS(app, supports_credentials=True)

    # Initialize SQLAlchemy
    db.init_app(app)

    # imports blueprints
    from super_admin_1.shop.del_shop import del_shop
    from super_admin_1.products.restore_product import restore_product
    from super_admin_1.products.restore_product import create_product # for testing purpose by Samuel Ogboye
    from super_admin_1.products.restore_product import delete_product # for testing purpose by Samuel Ogboye

    # register blueprints
    app.register_blueprint(del_shop)
    app.register_blueprint(restore_product)
    app.register_blueprint(create_product) # for testing purpose by Samuel Ogboye
    app.register_blueprint(delete_product) # for testing purpose by Samuel Ogboye


    # create db tables from models if not exists
    with app.app_context():
        db.create_all()

    return app
