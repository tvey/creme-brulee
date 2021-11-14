import factory
from django.contrib.auth import get_user_model
from faker import Faker

User = get_user_model()

fake = Faker('ru_RU')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.user_name()
    email = fake.email()
    password = factory.PostGenerationMethodCall('set_password', fake.password())
    is_active = True
