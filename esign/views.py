from rest_framework.viewsets import ModelViewSet
from .serializers import SignedDocumentSerializer, SignatureSerializer
from .models import SignedDocument, Signature


class SignedDocumentViewSet(ModelViewSet):
    queryset = SignedDocument.objects.all()
    serializer_class = SignedDocumentSerializer
    
class SignatureViewSet(ModelViewSet):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
