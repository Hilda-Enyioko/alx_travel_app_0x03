from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Luxury Beach House",
                "description": "A beautiful home with a sea view.",
                "price_per_night": 450.00,
                "location": "Cape Town",
                "max_guests": 6,
            },
            {
                "title": "Cozy Mountain Cabin",
                "description": "Perfect winter getaway with fireplace.",
                "price_per_night": 200.00,
                "location": "Nairobi",
                "max_guests": 4,
            },
            {
                "title": "Modern Apartment",
                "description": "City-center apartment with modern amenities.",
                "price_per_night": 150.00,
                "location": "Lagos",
                "max_guests": 3,
            },
        ]

        Listing.objects.all().delete()

        for item in sample_data:
            Listing.objects.create(**item)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
