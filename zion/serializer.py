from rest_framework import serializers
from zion.models import Currency

class CurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    currency_name = serializers.CharField()
    buy_price = serializers.FloatField()
    sell_price = serializers.FloatField()

    def create(self, validated_data):
        return Currency.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.currency_name = validated_data.get('currency_name', instance.currency_name)
        instance.buy_price = validated_data.get('buy_price',instance.buy_price)
        instance.sell_price = validated_data.get('sell_price',instance.sell_price)

        instance.save()
        return instance