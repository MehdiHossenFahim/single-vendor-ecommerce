from django.core.management.base import BaseCommand
from shop.models import Category, Product


class Command(BaseCommand):
    help = "Seed the database with real books for the Book Shop."

    def handle(self, *args, **options):
        categories = {
            "fiction": "Fiction",
            "non-fiction": "Non-Fiction",
            "sci-fi": "Sci-Fi & Fantasy",
            "children": "Children's Books",
        }

        cat_objs = {}

        for slug, name in categories.items():
            cat_objs[slug], _ = Category.objects.get_or_create(
                slug=slug,
                defaults={"name": name}
            )

        products = [
            # -------------------------
            # FICTION
            # -------------------------
            {
                "name": "The Great Gatsby",
                "category": "fiction",
                "price": 12.99,
                "description": (
                    "F. Scott Fitzgerald's classic novel about wealth, love, "
                    "ambition, and the American Dream in 1920s New York."
                ),
                "quantity": 25,
                "is_featured": True,
            },
            {
                "name": "1984",
                "category": "fiction",
                "price": 14.99,
                "description": (
                    "George Orwell's dystopian masterpiece about surveillance, "
                    "totalitarianism, truth, and individual freedom."
                ),
                "quantity": 30,
                "is_featured": True,
            },
            {
                "name": "To Kill a Mockingbird",
                "category": "fiction",
                "price": 15.50,
                "description": (
                    "Harper Lee's acclaimed novel exploring racial injustice, "
                    "morality, compassion, and childhood in the American South."
                ),
                "quantity": 20,
                "is_featured": True,
            },

            # -------------------------
            # NON-FICTION
            # -------------------------
            {
                "name": "Atomic Habits",
                "category": "non-fiction",
                "price": 18.99,
                "description": (
                    "James Clear's practical guide to building good habits, "
                    "breaking bad ones, and making small changes that produce "
                    "remarkable results."
                ),
                "quantity": 35,
                "is_featured": True,
            },
            {
                "name": "Sapiens",
                "category": "non-fiction",
                "price": 21.99,
                "description": (
                    "Yuval Noah Harari's sweeping exploration of human history, "
                    "from the emergence of Homo sapiens to the modern world."
                ),
                "quantity": 18,
                "is_featured": True,
            },
            {
                "name": "Educated",
                "category": "non-fiction",
                "price": 16.99,
                "description": (
                    "Tara Westover's memoir about education, family, "
                    "self-invention, and growing up in rural Idaho."
                ),
                "quantity": 15,
                "is_featured": False,
            },

            # -------------------------
            # SCI-FI & FANTASY
            # -------------------------
            {
                "name": "Dune",
                "category": "sci-fi",
                "price": 17.99,
                "description": (
                    "Frank Herbert's landmark science-fiction epic following "
                    "Paul Atreides on the desert planet Arrakis."
                ),
                "quantity": 28,
                "is_featured": True,
            },
            {
                "name": "The Hobbit",
                "category": "sci-fi",
                "price": 14.50,
                "description": (
                    "J.R.R. Tolkien's beloved fantasy adventure following "
                    "Bilbo Baggins on an unexpected journey with dwarves and Gandalf."
                ),
                "quantity": 22,
                "is_featured": True,
            },
            {
                "name": "Harry Potter and the Sorcerer's Stone",
                "category": "sci-fi",
                "price": 16.99,
                "description": (
                    "J.K. Rowling's magical adventure introducing Harry Potter "
                    "and his first year at Hogwarts School of Witchcraft and Wizardry."
                ),
                "quantity": 30,
                "is_featured": True,
            },

            # -------------------------
            # CHILDREN'S BOOKS
            # -------------------------
            {
                "name": "The Very Hungry Caterpillar",
                "category": "children",
                "price": 9.99,
                "description": (
                    "Eric Carle's classic picture book following a hungry "
                    "caterpillar as it eats its way through a variety of foods."
                ),
                "quantity": 40,
                "is_featured": True,
            },
            {
                "name": "Charlotte's Web",
                "category": "children",
                "price": 11.99,
                "description": (
                    "E.B. White's timeless story about the friendship between "
                    "a pig named Wilbur and a clever spider named Charlotte."
                ),
                "quantity": 25,
                "is_featured": True,
            },
            {
                "name": "The Little Prince",
                "category": "children",
                "price": 10.99,
                "description": (
                    "Antoine de Saint-Exupéry's beloved philosophical tale "
                    "about a young prince who travels between planets."
                ),
                "quantity": 35,
                "is_featured": False,
            },
        ]

        created = 0

        for p in products:
            _, was_created = Product.objects.get_or_create(
                name=p["name"],
                defaults={
                    "category": cat_objs[p["category"]],
                    "price": p["price"],
                    "description": p["description"],
                    "quantity": p["quantity"],
                    "is_featured": p["is_featured"],
                },
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(cat_objs)} categories and {created} new products."
            )
        )
