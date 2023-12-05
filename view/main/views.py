from django.shortcuts import render, redirect
from .models import Log_table
from .forms import Log_tableForm


def start(request):
    if request.method == 'POST':
        error = ''
        form = Log_tableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
        else:
            error = 'not right'

    form = Log_tableForm()

    data = {
        'form': form
    }
    return render(request, 'main/start.html', data)


def defined(request):
    form = Log_tableForm()

    data = {
        'form': form
    }
    return render(request, 'main/changed.html', data)


def result(request):
    return render(request, 'main/success.html')


def entrylogs(request):
    logs = Log_table.objects.order_by('-log_time')
    return render(request, 'main/logs.html', {'logs': logs})
