from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from wifi_ui.wifi_scan import get_single, get_essid, get_wifi_list, connect_wifi,get_result


def index(request):
    connected_ap = get_wifi_list()
    essid_list = get_essid()
    single_list = get_single()
    #return render(request, "test.html")
    return render(request, 'index.html', {'essid_list': essid_list, 'single_list': single_list,
                                          'connected_ap': connected_ap})


def connect(request):
    essid = request.GET.get('essid')
    string = essid
    if request.POST:
        passwd = request.POST.get('passwd')
        connect_wifi(essid, passwd)

    result = get_result()
    if result == essid:
        flag = 0
    else:
        flag = 1
    print(result)
    return render(request, 'ui/connect.html', {'string': string, 'result': result, 'flag':flag })

