from rest_framework import serializers
from .models import *

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=LogEntry
        fields=('level','log_string','timestamp','source')
        
class CreateLogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model=LogEntry
        fields=('level','log_string','timestamp','source')

        
