from django_seed import Seed
from products.models import Product

seeder = Seed.seeder()

seeder.add_entity(Product, 10, {
    'name': lambda x: seeder.faker.first_name(),
    'price': lambda x: random.randint(0,1000),
    'quantity': lambda x: random.randint(0,1000),
})


seeder.execute()
