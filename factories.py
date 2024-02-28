
"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    id = factory.Sequence(lambda n: n)
       name = FuzzyChoice(
        choices=[
            "Tshirt",
            "Shirt",
            "Skirt",
            "Lehenga",
            "Sari",
            "Shorts",
            "Towels",
            "Brush",
            "Apple",
            "Bannar",
            "Lemon",
            "Hammer",
        ]
    )
    description = factory.Faker("text")
    price = FuzzyDecimal(0.5, 2000.0, 2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.TOOLS,
        ]
    )