from rest_framework import serializers
from .models import Candidate, Contact
from django.db import transaction
from django.db.models import Max


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ["created_at", "candidate"]

    def create(self, validated_data):
        candidate = self.context['candidate']
        contact = Contact.objects.create(
            candidate=candidate,
            **validated_data
        )

        return contact

class CandidateSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField(read_only=True)
    last_update = serializers.SerializerMethodField(read_only=True)
    last_update_contact = serializers.SerializerMethodField(read_only=True)

    def get_contacts(self, obj):
        return ContactSerializer(obj.contact_set.all(), many=True).data
    
    def get_last_update(self, obj):
        return obj.updated_at
    
    def get_last_update_contact(self, obj):
        last_date = obj.contact_set.all().aggregate(
            date=Max("updated_at")
        )
        return last_date["date"]

    class Meta:
        model = Candidate
        fields = [
            "id", "name", "sobrenome", "document", "type_document", "job", 
            "last_update", "last_update_contact", "contacts"
        ]