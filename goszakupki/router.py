from tenders.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('procuring_organ', ProcuringOrganViewSet)
router.register('participants', ParticipantsViewSet)
router.register('redflags', RedFlagsViewSet)
router.register('tenders', TenderViewSet)