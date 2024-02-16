
from rest_framework import serializers
from datetime import date


class LineItemDTO(serializers.Serializer):
    quantity = serializers.FloatField()
    price = serializers.FloatField()


class InvoiceDTO(serializers.Serializer):
    date = serializers.DateField(default=date.today().strftime("%d/%m/%y"))
    amount = serializers.FloatField(default=0)
    customer_name = serializers.CharField(max_length=200)
    invoice_number = serializers.IntegerField()
    line_items = LineItemDTO(many=True)
