from rest_framework import serializers
from .models import SignedDocument, Signature


class SignedDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignedDocument
        fields = '__all__'
        
        
class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = '__all__'