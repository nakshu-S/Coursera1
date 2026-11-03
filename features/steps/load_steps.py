
from behave import given
from service.models import Product


@given('the following products')
def step_impl(context):
    """Load background product data."""

    for row in context.table:
        product = Product(
            name=row['name'],
            description=row['description'],
            price=float(row['price']),
            category=row['category'],
            available=row['available'].lower() == 'true'
        )

        product.create()
