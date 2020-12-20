from django.shortcuts import render
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
	data = Pengunjung(address=address).save()
	pengunjung = Pengunjung.objects.all().order_by('-tanggal')[:10]
	context = {
		'ip': address,
		'pengunjung': pengunjung,
		'tersedia': pengunjung.exists(),
	}
	return render(request, 'index.html', context)
