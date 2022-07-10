from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields='__all__'

    # def save(self):
    #     account = Account(
    #         email_id=self.validated_data['email_id'],
    #         account_id=self.validated_data['account_id'],

    #     )
    #     account_name=self.validated_data['account_name']
    #     account.save()
    #     return account

