from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE


User = get_user_model()


class Order(models.Model):
    # 마켓컬리를 기준으로 모델을 짠다.
    # created_at 주문 날짜를 확인하기 위해
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    # 주문을 한 유저
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # 배송지 -> 받으실 장소 포함
    address = models.ForeignKey(
        'members.UserAddress',
        on_delete=models.CASCADE,
    )

    # 결제 금액
    def total_payment(self):
        payment = 0
        for ins in self.item.all():
            payment += ins.sub_total()
        return payment
