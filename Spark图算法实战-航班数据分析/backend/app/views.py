from django.shortcuts import render
from app.models import AirData
from django.http import JsonResponse
from django.http import HttpResponse
import json
from collections import defaultdict
import requests
import networkx as nx
import csv

# Create your views here.


def test(request):
    data = AirData.objects.filter(flight_num='1')
    data = json.dumps(data)
    return HttpResponse(data)


def getedges(request):
    graph = nx.Graph()
    data = AirData.objects.values('dep_airport', 'arr_airport')
    for it in data:
        a = it['dep_airport']
        b = it['arr_airport']
        if graph.has_edge(a, b) or graph.has_edge(b, a):
            continue
        if a == 'JFK' or a == 'ATL' or b == 'ATL' or b == 'JFk':
            graph.add_edge(a, b)
    edges = list(graph.edges())
    # print(graph.number_of_edges())
    return JsonResponse({
        'result': 'success',
        'data': edges
    })


def popular(resquest):
    # data = AirData.objects.all()
    # mp = defaultdict(int)
    # for air in data:
    #     mp[air.dep_airport] += 1
    #     mp[air.arr_airport] += 1

    # res = sorted(mp.items(), key=lambda x: x[1], reverse=True)[:10]

    res = [['ATL', 56500], ['DFW', 45352], ['LAX', 35926], ['ORD', 35655], ['DEN', 34361],
           ['IAH', 26697], ['PHX', 26180], ['SFO', 26125], ['LAS', 21646], ['CLT', 18685]]

    # res = json.dumps(mp)
    return JsonResponse({
        'result': 'success',
        'data': res
    })


def airline(request):
    origin = request.GET.get('origin')
    dest = request.GET.get('dest')
    data = AirData.objects.filter(dep_airport=origin, arr_airport=dest)
    mp = defaultdict(int)
    for air in data:
        mp[air.at_month] += 1
    res = sorted(mp.items(), key=lambda x: int(x[0]))
    return JsonResponse({
        'result': 'sueecss',
        'data': res
    })


def delay(request):
    air_port = request.GET.get('air_port')
    data = AirData.objects.filter(dep_airport=air_port, fly_delay__gt=0)
    mp = defaultdict(int)
    for air in data:
        mp[air.at_month] += 1
    res = sorted(mp.items(), key=lambda x: int(x[0]))
    return JsonResponse({
        'result': 'success',
        'data': res
    })


def tendelay(request):
    airports = ['ATL', 'DFW', 'LAX', 'ORD',
                'DEN', 'IAH', 'PHX', 'SFO', 'LAS', 'CLT']
    delay_cnt = defaultdict(int)
    notdelay_cnt = defaultdict(int)
    for airport in airports:
        all = AirData.objects.filter(dep_airport=airport).count()
        delay = AirData.objects.filter(
            dep_airport=airport, fly_delay__gt=0).count()
        delay_cnt[airport] = delay
        notdelay_cnt[airport] = all - delay
    return JsonResponse({
        'result': 'success',
        'data': {
            'delay': delay_cnt,
            'notdelay': notdelay_cnt
        }
    })


def getusa(request):
    response = requests.get(
        'https://echarts.apache.org/examples/data/asset/geo/USA.json', verify=False, proxies={'https': None})
    map_data = response.json()
    return JsonResponse(map_data)


def getshortest(request):
    origin = request.GET.get('origin')
    dest = request.GET.get('dest')

    graph = nx.DiGraph()
    data = AirData.objects.values(
        'dep_airport', 'arr_airport', 'exp_flight_time')

    for it in data:
        a = it['dep_airport']
        b = it['arr_airport']
        c = int(it['exp_flight_time'])
        if not graph.has_edge(a, b):
            graph.add_edge(a, b, weight=c)

    try:
        shortest_paths = list(nx.all_shortest_paths(
            graph, origin, dest, weight='weight'))
        return JsonResponse({
            'result': 'success',
            'data': shortest_paths
        })
    except Exception as e:
        return JsonResponse({
            'result': 'success',
            'data': []
        })


def getcheapest(request):
    origin = request.GET.get('origin')
    dest = request.GET.get('dest')

    graph = nx.DiGraph()
    data = AirData.objects.values(
        'dep_airport', 'arr_airport', 'fly_dist')

    for it in data:
        a = it['dep_airport']
        b = it['arr_airport']
        c = int(it['fly_dist'])
        if not graph.has_edge(a, b):
            graph.add_edge(a, b, weight=180 + 0.15 * c)

    try:
        cheapest_paths = list(nx.all_shortest_paths(
            graph, origin, dest, weight='weight'))
        return JsonResponse({
            'result': 'success',
            'data': cheapest_paths
        })
    except Exception as e:
        return JsonResponse({
            'result': 'success',
            'data': []
        })


def getimportant(request):
    G = nx.DiGraph()
    data = AirData.objects.values('dep_airport', 'arr_airport')
    for it in data:
        a = it['dep_airport']
        b = it['arr_airport']
        G.add_edge(a, b)

    try:
        # pagerank_score = nx.pagerank(graph)
        # most_important_route = max(pagerank_score, key=pagerank_score.get)

        # edge_betweenness = nx.edge_betweenness_centrality(graph)

        # # 找出介数中心性最高的边
        # max_betweenness = max(edge_betweenness.values())
        # important_edges = [edge for edge, betweenness in edge_betweenness.items(
        # ) if betweenness == max_betweenness]

        pagerank = nx.pagerank(G)

# 找出具有最高 PageRank 值的边
        most_important_edge = max(G.edges, key=lambda e: pagerank[e[1]])

        return JsonResponse({
            'result': 'success',
            'data': most_important_edge
        })
    except Exception as e:
        return JsonResponse({
            'result': str(e)
        })


def air_location(request):

    return JsonResponse({
        'result': 'success'
    })
