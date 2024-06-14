from django.db import models
from account.models import CustomUser

class Subscription(models.Model):
  PLAN_CHOICES = [
        ('basic', 'Basic Plan'),
        ('premium', 'Premium Plan'),
    ]
  
  subscriber_name = models.CharField(max_length=120)
  subscriber_plan = models.CharField(max_length=250, choices= PLAN_CHOICES)
  subscriber_cost = models.CharField(max_length=250)
  paypal_sub_id =  models.CharField(max_length=255)
  is_active = models.BooleanField(default=False)
  user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, unique=True)

  def __str__(self):
      return f"{self.subscriber_name} - {self.subscriber_plan} subscription"
  