from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Resolver import resolver_ecuacion_latex as relatex


@api_view([ 'POST'])
def my_view(request):
    methods = {
        'POST':lambda: relatex(request)
    }
    response_data = methods[request.method]()
    return Response(response_data)