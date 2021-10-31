from django.core.management.base import BaseCommand
from cowork.models import Store, Seat

# python manage.py create_initial_store
# で実行
class Command(BaseCommand):
  def handle(self, *args, **options):
    store = Store.objects.create(address='愛媛県松山市あああああ', name="Voice")
    store.save()

    seat_1 = Seat(number=1, store=store)
    seat_1.save()

    seat_2 = Seat(number=1, store=store)
    seat_2.save()

    seat_3 = Seat(number=1, store=store)
    seat_3.save()

    seat_4 = Seat(number=1, store=store)
    seat_4.save()

    seat_5 = Seat(number=2, store=store)
    seat_5.save()

    seat_6 = Seat(number=2, store=store)
    seat_6.save()

    seat_7 = Seat(number=4, store=store)
    seat_7.save()

    seat_8 = Seat(number=4, store=store)
    seat_8.save()

    seat_9 = Seat(number=8, store=store)
    seat_9.save()

    seat_10 = Seat(number=8, store=store)
    seat_10.save()

