from rest_framework import serializers

from .models import Status


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Status.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance