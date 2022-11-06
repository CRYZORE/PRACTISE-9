from django.http import HttpResponse
import summary.sum

# Create your views here.


def index(request, s):
    return HttpResponse(f'<h1>Сумма чисел равна {summary.sum.summary(s)}</h1>')