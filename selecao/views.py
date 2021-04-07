from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .serializers import CandidateSerializer, ContactSerializer
from .models import Candidate, Contact
# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all().order_by("-created_at")

    @action(
        methods=['post'],
        url_path='contact/add',
        detail=True        
    )
    def add_contact(self, request, pk=None):
        try:
            candidate = Candidate.objects.get(pk=pk)
            serializer = ContactSerializer(
                data=request.data, context={'candidate': candidate}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Candidate.DoesNotExist:
            return Response({
                'id':"Candidato não encontrado!"
            }, status=status.HTTP_404_NOT_FOUND)

class ContactViewSet(generics.UpdateAPIView, viewsets.GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by("-created_at")