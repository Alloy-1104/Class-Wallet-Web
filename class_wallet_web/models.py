from django.db import models

# Create your models here.

class Purchase(models.Model):
    label = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    sum_price = models.PositiveIntegerField(
        blank=False,
        null=False
    )

    def __str__(self):
        return self.label

class Part(models.Model):
    PART_TYPES = (("exhibition", "展示"), ("lantern", "行燈"), ("banner", "垂れ幕"), ("cm", "クラスCM"))
    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        choices=PART_TYPES,
        default=PART_TYPES[0][0]
    )
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def __str__(self):
        return self.name