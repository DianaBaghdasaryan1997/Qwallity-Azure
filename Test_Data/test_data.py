from faker import Faker
fake = Faker()

credentials = {
    "name": fake.name(),
    "email": fake.email(),
    "username": fake.user_name(),
    "password": fake.password(length=8)
}