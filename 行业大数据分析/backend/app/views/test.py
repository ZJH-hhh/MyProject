from django.http import JsonResponse

def test(request):
    res = '124'
    return JsonResponse({
        'result': 'success',
        'data': res,
    })
