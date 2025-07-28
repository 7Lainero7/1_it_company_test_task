import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.dds.models import Status, TransactionType, Category, SubCategory, CashFlowRecord

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Seed random CashFlowRecord data"

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=20, help="Number of records to create")

    def handle(self, *args, **options):
        count = options["count"]
        statuses = list(Status.objects.all())
        types = list(TransactionType.objects.all())
        categories = list(Category.objects.select_related("type"))
        subcategories = list(SubCategory.objects.select_related("category"))

        if not (statuses and types and categories and subcategories):
            self.stdout.write(self.style.ERROR("Not enough data: make sure Status, TransactionType, Category, and SubCategory are populated"))
            return

        created = 0
        for _ in range(count):
            status = random.choice(statuses)
            type_ = random.choice(types)

            # Найдём категории, подходящие к типу
            valid_categories = [c for c in categories if c.type_id == type_.id]
            if not valid_categories:
                continue

            category = random.choice(valid_categories)

            # Найдём подкатегории, подходящие к категории
            valid_subcategories = [s for s in subcategories if s.category_id == category.id]
            if not valid_subcategories:
                continue

            subcategory = random.choice(valid_subcategories)

            CashFlowRecord.objects.create(
                status=status,
                type=type_,
                category=category,
                subcategory=subcategory,
                amount=round(random.uniform(100, 10000), 2),
                comment=fake.sentence(nb_words=6)
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Created {created} CashFlowRecord(s)"))
