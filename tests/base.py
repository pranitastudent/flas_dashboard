Learn more or give us feedback
from flask.ext.testing import TestCase

from project import app, db
from dashboard.models import Customer, Order, Product, User

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def tearDown(self):
        db.session.remove()
        db.drop_all()