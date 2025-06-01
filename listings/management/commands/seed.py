from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Number of listings to create
            title = fake.sentence(nb_words=3)
            description = fake.paragraph(nb_sentences=5)
            location = fake.city()
            price_per_night = round(random.uniform(50, 500), 2)

            listing = Listing.objects.create(
                title=title,
                description=description,
                location=location,
                price_per_night=price_per_night
            )

            listing.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample listings data.'))

