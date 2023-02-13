from .models import *
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ["password"]
        # fields=['first_name','last_name','mobile','email','password','is_active','is_admin','is_staff','count','id']