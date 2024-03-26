from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SignedDocument(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    file = models.FileField(upload_to='documents/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
class Signature(models.Model):
    document = models.OneToOneField(SignedDocument, related_name='signature', on_delete=models.CASCADE, blank=True)
    sign = models.ImageField(upload_to='signatures/', blank=True)
    signer = models.CharField(max_length=100, blank=True, default='')
    verified = models.BooleanField(default=False, blank=True)
    verified_by = models.ForeignKey(User, related_name='verifier', on_delete=models.SET_NULL, null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
