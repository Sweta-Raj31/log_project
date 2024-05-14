

from django.contrib import admin
from .models import LogEntry

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('level', 'log_string', 'timestamp', 'source')
    list_filter = ('level', 'timestamp', 'source')
    search_fields = ('log_string', 'source')

admin.site.register(LogEntry, LogEntryAdmin)

