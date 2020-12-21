from django.http import HttpResponse

from index.models import Pengunjung


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    address = get_client_ip(request)
    Pengunjung(address=address).save()
    return HttpResponse(address)
