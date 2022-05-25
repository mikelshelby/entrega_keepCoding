from rest_framework import serializers
from entries.models import Entry
from dataclasses import dataclass


class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    datetime = serializers.DateTimeField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    
    def create(self, validated_data):
        # Voy a salvar a validated dataclass
        instance = Entry(
            datetime = validated_data.get("datetime"),
            concept = validated_data.get("concept"),
            amount = validated_data.get("amount"),
        )

        instance.save()

        return instance
    
    def update(self, instance, validated_data):
        # Voy a modificar instancia con validated data
        instance.datetime = validated_data.get("datetime")
        instance.concept = validated_data.get("concept")
        instance.amount = validated_data.get("amount")

        instance.save()
        return instance
