# seed.py

from app import app
from models import db, Book
from datetime import date

def seed_data():
    with app.app_context():
        if Book.query.count() > 0:
            print("⚠️ Books already exist. Skipping seeding.")
            return

        books = [
            Book(
                title="The Pragmatic Programmer",
                author="Andrew Hunt, David Thomas",
                genre="Programming",
                description="Classic book on software craftsmanship.",
                isbn="9780201616224",
                published_date=date(1999, 10, 20)
            ),
            Book(
                title="Clean Code",
                author="Robert C. Martin",
                genre="Programming",
                description="A handbook of agile software craftsmanship.",
                isbn="9780132350884",
                published_date=date(2008, 8, 1)
            ),
            Book(
                title="Atomic Habits",
                author="James Clear",
                genre="Self-help",
                description="An easy & proven way to build good habits & break bad ones.",
                isbn="9780735211292",
                published_date=date(2018, 10, 16)
            ),
            Book(
                title="Sapiens: A Brief History of Humankind",
                author="Yuval Noah Harari",
                genre="History",
                description="Explores the history and impact of Homo sapiens.",
                isbn="9780062316097",
                published_date=date(2011, 1, 1)
            ),
            Book(
                title="The Lean Startup",
                author="Eric Ries",
                genre="Business",
                description="How today's entrepreneurs use continuous innovation.",
                isbn="9780307887894",
                published_date=date(2011, 9, 13)
            )
        ]

        db.session.bulk_save_objects(books)
        db.session.commit()
        print("✅ Dummy books inserted.")

if __name__ == '__main__':
    seed_data()
