from typing import ValuesView
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response


class ProcuringOrganViewSet(viewsets.ModelViewSet):
    queryset = ProcuringOrganization.objects.all()
    serializer_class = ProcuringOrganSerializer

class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer

class RedFlagsViewSet(viewsets.ModelViewSet):
    queryset = RedFlags.objects.all()
    serializer_class = RedFlagSerializer

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all()
    serializer_class = TenderSerialzer

    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(TenderViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='home.html')
        return response 

    