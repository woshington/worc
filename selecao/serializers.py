from rest_framework import serializers
from .models import Candidate, Contact
from django.db import transaction

class CandidateSerializer(serializers.ModelSerializer):
    type_phone = serializers.CharField(write_only=True)
    number = serializers.CharField(write_only=True)
    contacts = serializers.SerializerMethodField(read_only=True)

    def get_contacts(self, obj):
        return ContactSerializer(obj.contact_set.all(), many=True).data

    class Meta:
        model = Candidate
        fields = [
            "name", "sobrenome", "document", "type_document", "job", "contacts",
            "type_phone", "number"
        ]

    def validate(self, attrs):
        choices = dict(Contact.TYPE_CHOICES)
        if not attrs['type_phone'] in choices:
            raise serializers.ValidationError({
                'type_phone': 'Tipo telefone inválido!'
            })
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        type_phone = validated_data.pop("type_phone")
        number = validated_data.pop("number")
        candidate = Candidate.objects.create(
            **validated_data
        )

        obj = Contact(type=type_phone, number=number, candidate=candidate)
        obj.save()

        return candidate


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        exclude = ["created_at", "updated_at"]