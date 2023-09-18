from django.http import JsonResponse
from collections import defaultdict

import chardet
import pandas as pd


def timePredict(request):
    job = request.GET.get('job')
    city = request.GET.get('city')

    file_path = 'app/media/predicted_salaries.csv'
    with open(file_path, 'rb') as f:
        detected_encoding = chardet.detect(f.read())['encoding']

    df = pd.read_csv(file_path, encoding=detected_encoding)

    df = df[(df['城市'] == city) & (df['关键字'] == job)]
    # data = data.iloc[1:].reset_index(drop=True)
    # data = data.to_json(orient='records')
    mp = defaultdict(float)
    months = ['二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月预测']
    for index, row in df.iterrows():
        for month in months:
            mp[month] = row[month]

    data = list(mp.items())
    # print(data)
    return JsonResponse({
        'result': 'success',
        'data': data
    })
