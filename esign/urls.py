from rest_framework.routers import SimpleRouter
from .views import SignedDocumentViewSet, SignatureViewSet

router = SimpleRouter()

router.register('signed-doc', SignedDocumentViewSet)
router.register('signature', SignatureViewSet)

urlpatterns = router.urls