from django.shortcuts import render

# Create your views here.


from .models import TempMeasurement, Logs


def index(request):
    temp_measurement = TempMeasurement.objects.all()
    # log request
    Logs.objects.create(method=request.method, url=request.build_absolute_uri())
    context = {'temp_measurement': temp_measurement}
    return render(request, 'index.html', context)
