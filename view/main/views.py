from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Log_table
from .forms import Log_tableForm, Log_tableForm2
from .make_video import make_video
from wsgiref.util import FileWrapper
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def start(request):
    error = ''
    if request.method == 'POST':
        form = Log_tableForm2(request.POST)
        if form.is_valid():
            form.save()
            for log in Log_table.objects.order_by('-log_time'):
                make_video(log.text)
                break
            return redirect('result')
        else:
            error = 'not right'

    form = Log_tableForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/start.html', data)


@csrf_exempt
def defined(request):
    error = ''
    if request.method == 'POST':
        form = Log_tableForm(request.POST)
        if form.is_valid():
            form.save()
            for log in Log_table.objects.order_by('-log_time'):
                make_video(log.text, log.height, log.width,
                           user_scale=log.scale, user_thickness=log.thickness)
                break
            return redirect('result')
        else:
            error = 'not right'

    form = Log_tableForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/changed.html', data)


@csrf_exempt
def result(request):
    file = FileWrapper(open('main/media/main/result.mp4', 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=your_string.mp4'
    return response


def entrylogs(request):
    logs = Log_table.objects.order_by('-log_time')
    return render(request, 'main/logs.html', {'logs': logs})
