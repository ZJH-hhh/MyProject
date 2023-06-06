from rest_framework import viewsets
from app.models.jobs import Jobs
from app.serializer import JobsSerializer
from rest_framework.response import Response
from rest_framework import status


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        params_dict = request.GET.dict()
        if params_dict:
            key = next(iter(request.GET.keys()))
            val = request.GET.get(key)
            if key == 'jobname':
                key = 'name'
            elif key == 'jobid':
                key = 'id'
            if val != 'all':
                self.queryset = self.queryset.filter(**{key: val})
        # jobname = request.GET.get('jobname')
        # if jobname:
        #     if jobname != 'all':
        #         self.queryset = self.queryset.filter(name=jobname)
        # else:
        #     jobid = request.GET.get('jobid')
        #     if jobid:
        #         self.queryset = self.queryset.filter(id=jobid)

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
