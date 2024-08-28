from django.shortcuts import render

def payment_process(request):
    return render(request, 'payment/process.html')

def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')