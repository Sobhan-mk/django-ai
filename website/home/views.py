from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        pld_detector_url = 'PLDdetector:detector_model'
    else:
        pld_detector_url = 'accounts:login'

    context = {'pld_detector_url': pld_detector_url}
    return render(request, 'home/home.html', context)
