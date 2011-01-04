from django.http import HttpResponse, HttpResponseRedirect

def set_language(request):
    if request.method == "GET":
        request.session['django_language'] = request.GET.get('language', 'en')
            
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def test(request):
    return HttpResponse("TEST2")
