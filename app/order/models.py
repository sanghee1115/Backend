from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

User = get_user_model()


class Order(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    address = models.ForeignKey('members.UserAddress', on_delete=models.CASCADE)

    def total_payment(self):
        payment = 0
        for ins in self.item.all():
            payment += ins.sub_total()
        return payment
