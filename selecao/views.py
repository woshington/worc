from rest_framework import viewsets
from .serializers import CandidateSerializer
from .models import Candidate
# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    # permission_classes = (AllowAny, )
    queryset = Candidate.objects.all().order_by("-created_at")
