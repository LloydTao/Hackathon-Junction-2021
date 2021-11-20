from rest_framework import routers
from messaging.viewsets import RoomViewSet, MessageViewSet

router = routers.DefaultRouter()

router.register(r"rooms", RoomViewSet)
router.register(r"messages", MessageViewSet)
