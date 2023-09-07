from collections import defaultdict
from django.http import JsonResponse

import csv


def typeScore(request):
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
            skills = line[8].split()
            for skill in skills:
                mp[skill] += score
                cnt[skill] += 1
    avg = defaultdict(float)
    for k, v in mp.items():
        if cnt[k] < 100:
            continue
        avg[k] = v / cnt[k]
    data = sorted(list(avg.items()), key=lambda x: x[1], reverse=True)[:10]
    # print(data)
    # print('数据分析', mp['数据分析'], cnt['数据分析'], avg['数据分析'])
    # print('网络货运 {} {}'.format(mp['网络货运'], cnt['网络货运']))

    return JsonResponse({
        'result': 'success',
        'data': data
    })
