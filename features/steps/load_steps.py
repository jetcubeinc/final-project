from behave import given
from app import db
from app.models import ProductModel

@given('the following products exist')
def step_impl(context):
    for row in context.table:
        product = ProductModel(
            name=row['name'],
            category=row['category'],
            price=float(row['price']),
            available=row['available'].lower() == 'true'
        )
        db.session.add(product)
    db.session.commit()
