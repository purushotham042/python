from rest_framework import serializers
from .models import STUDENT


class STUDENTSerializer(serializers.ModelSerializer):
    class Meta:
        model = STUDENT
        fields = '__all__'

    def create(self, validated_data):
        return STUDENT.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('pk', instance.pk)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.qualification = validated_data.get('qualification', instance.qualifiation)
        instance.mail_id = validated_data.get('mail_id', instance.mail_id)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.joining_date = validated_data.get('joining_date', instance.joining_date)
        instance.balance_amount = validated_data.get('balance_amount', instance.balance_amount)
        instance.save()
        return instance

