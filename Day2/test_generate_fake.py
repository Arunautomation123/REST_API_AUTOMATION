from faker import Faker

class TestFakeData:
    """Faker class with fake data"""
    def test_fake_data_generator(self):
        fake = Faker()
        name = fake.name()
        print(name)
        print(fake.first_name(), fake.last_name())
        print(fake.password(length=10, special_chars=True))
        print(fake.email())
        print(fake.phone_number())