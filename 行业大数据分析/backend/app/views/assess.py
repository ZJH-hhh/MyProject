from collections import defaultdict
from django.http import JsonResponse

import csv


def assess(request):
    mp = defaultdict(int)
    with open('app/scored_job_data.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        i = 0
        for line in csv_reader:
            i += 1
            if i == 1:
                continue
            val = float(line[10][:-1])
            mp[val] += 1
    data = sorted(list(mp.items()), key=lambda x: x[0])

    return JsonResponse({
        'result': 'success',
        'data': data
    })
