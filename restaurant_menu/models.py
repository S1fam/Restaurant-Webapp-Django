from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    ("starters", "Starters"),  # (backend, frontend),
    ("salads", "Salads"),
    ("main_dishes", "Main dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    meal = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=100, choices=MEAL_TYPE)
    # User (cook) gets associated with 1+ Items (meals), on delete of a user all his meals
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # are either
    # protected as is his name (PROTECT)/ deleted (.CASCADE)/ user set on null (.SET_NULL)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)  # timestamp of creation
    date_updated = models.DateTimeField(auto_now=True)  # timestamp of last update

    def __str__(self):
        return self.meal
