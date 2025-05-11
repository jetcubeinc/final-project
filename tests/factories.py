import factory
import random
from app import db
from app.models import ProductModel

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = ProductModel
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker("word")
    category = factory.Iterator(["Electronics", "Books", "Clothing", "Toys", "Home"])
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    available = factory.LazyFunction(lambda: random.choice([True, False]))
