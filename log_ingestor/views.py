from django.shortcuts import render
import logging
from django.db.models import Q
from django.http import HttpResponseBadRequest, JsonResponse

from rest_framework.views import APIView
from rest_framework import generics, status
from .models import *
from rest_framework.response import Response
from .serializer import *
from datetime import datetime



class ReactView(APIView):
    serializer_class = CreateLogEntrySerializer
    
            
    def post(self,request):
        serializer = CreateLogEntrySerializer(data=request.data)
        # add emailvalidator
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

  

# Create your views here.





def log_api(request):
    level = request.POST.get('level')
    log_string = request.POST.get('log_string')
    timestamp = request.POST.get('timestamp')
    source = request.POST.get('source')

    # Check if 'level' is provided and not None
    if level is None:
        return HttpResponseBadRequest('Log level is required')

    # Validate the log level
    valid_levels = ['info', 'error', 'success']
    if level.lower() not in valid_levels:
        return HttpResponseBadRequest('Invalid log level')

    logger = logging.getLogger(source)
    logger.setLevel(logging.getLevelName(level.upper()))

    logger.log(logging.getLevelName(level.upper()), log_string)

    return JsonResponse({'message': 'Log created successfully'})








def query_interface(request):
    logs = LogEntry.objects.all()

    # Apply filters
    level = request.GET.get('level')
    log_string = request.GET.get('log_string')
    timestamp = request.GET.get('timestamp')
    source = request.GET.get('source')

    if level:
        logs = logs.filter(level=level)
    if log_string:
        logs = logs.filter(log_string__icontains=log_string)
    if timestamp:
        logs = logs.filter(timestamp=timestamp)
    if source:
        logs = logs.filter(metadata__source=source)

    return render(request, 'query.html', {'logs': logs})



def sample_queries(request):
    if request.method == 'GET':
        query_type = request.GET.get('query_type')
        if query_type == 'error_logs':
            logs = LogEntry.objects.filter(level='error')
        elif query_type == 'search_logs':
            term = request.GET.get('term')
            logs = LogEntry.objects.filter(log_string__icontains=term)
        elif query_type == 'date_range_logs':
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            logs = LogEntry.objects.filter(timestamp__range=[start_date, end_date])
        else:
            return JsonResponse({'error': 'Invalid query type'})

        return JsonResponse({'logs': logs})


def advanced_search(request):
    level = request.GET.get('level')
    log_string = request.GET.get('log_string')
    timestamp_start = request.GET.get('timestamp_start')
    timestamp_end = request.GET.get('timestamp_end')
    source = request.GET.get('source')

    query = Q()
    if level:
        query &= Q(level=level)
    if log_string:
        query &= Q(log_string__icontains=log_string)
    if timestamp_start and timestamp_end:
        query &= Q(timestamp__range=[timestamp_start, timestamp_end])
    if source:
        query &= Q(source=source)

    logs = LogEntry.objects.filter(query)

    return render(request, 'advanced_search.html', {'logs': logs})





def check_logs(request):
    # Retrieve query parameters
    level = request.POST.get('level')
    log_string = request.POST.get('log_string')
    source = request.POST.get('source')

    # Retrieve date range parameters
    start_date_str = request.POST.get('start_date')
    end_date_str = request.POST.get('end_date')

    # Convert date strings to datetime objects
    start_date = datetime.fromisoformat(start_date_str)
    end_date = datetime.fromisoformat(end_date_str)

    # Query logs based on provided criteria and date range
    logs_available = LogEntry.objects.filter(
        level=level,
        log_string__icontains=log_string,
        source=source,
        timestamp__range=(start_date, end_date)
    ).exists()

    if logs_available:
        return JsonResponse({'message': 'Logs found', 'logs_available': True})
    else:
        return JsonResponse({'message': 'No logs found', 'logs_available': False})

# def ingest_log(request, api_name):
#   # Get log data from request (replace with actual logic for your APIs)
#   log_data = json.loads(request.body)

#   # Extract relevant fields
#   level = log_data.get('level', 'info')
#   log_string = log_data.get('log_message')
#   timestamp = log_data.get('timestamp')  # Might need conversion
  # source_file = f"log{api_name}.log"  # Assuming log files named based on API

  # # Error handling (replace with more robust logic)
  # if not log_string:
  #   return HttpResponse(status=400)

  # # Save log entry
  # LogEntry.objects.create(
  #     level=level,
  #     log_string=log_string,
  #     timestamp=timestamp,
  #     metadata={'source': source_file}
  # )

  # return HttpResponse(status=201)
