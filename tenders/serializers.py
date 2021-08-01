from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProcuringOrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcuringOrganization
        fields = '__all__'

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'

class RedFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedFlags
        fields = '__all__'

class TenderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = '__all__'

