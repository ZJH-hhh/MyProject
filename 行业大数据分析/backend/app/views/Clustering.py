from collections import defaultdict
from django.http import JsonResponse

import pandas as pd


def clustering(request):
    df = pd.read_csv('app/media/cluster.csv')
    data = df[['Cluster', 'X', 'Y']]
    data = data.to_json(orient='records')

    return JsonResponse({
        'result': 'success',
        'data': data,
    })
