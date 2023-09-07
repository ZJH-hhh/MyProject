from collections import defaultdict
from django.http import JsonResponse

import csv
import random


def cityScore(request):
    mp = defaultdict(float)
    cnt = defaultdict(int)
    with open('app/scored_job_data.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        i = 0
        for line in csv_reader:
            i += 1
            if i == 1:
                continue
            score = float(line[10])
            city = line[1][:2]
            mp[city] += score
            cnt[city] += 1
    avg = defaultdict(float)
    for k, v in mp.items():
        # if cnt[k] < 100:
        #     continue
        avg[k] = v / cnt[k]
    data = sorted(list(avg.items()), key=lambda x: x[1], reverse=True)[:10]
    # random.shuffle(data)

    return JsonResponse({
        'result': 'success',
        'data': data
    })
