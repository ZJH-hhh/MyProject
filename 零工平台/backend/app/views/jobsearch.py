from rest_framework.views import APIView
from rest_framework. response import Response
from app.models.jobs import Jobs


class JobsView(APIView):
    def get(self, request):
        name = request.GET.get('name')
        jobs = Jobs.objects.filter(name=name)
        return Response({
            'result': 'sueecss',
            'data': jobs,
        })
