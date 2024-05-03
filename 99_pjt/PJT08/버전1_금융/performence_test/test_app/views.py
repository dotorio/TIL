from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import csv
import numpy as np
import pandas as pd

array_length = 1000
random_range = 5000

df = pd.read_csv('data/test_data.CSV', encoding='cp949')
df.fillna('NULL')

data = df.to_dict('records')
age_avg = df['나이'].mean()
def get_data(request):
    # ages = []
    # # print(data)
    # for age in data:
    #     ages.append(age)

    

    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False})

def result_age_avg(request):
    
    
    new_data = []
    for person in df.itertuples():
        new_data.append(list(person[1:]))
    new_data.sort(key = lambda x:abs(x[1]-age_avg))
    new_df = pd.DataFrame(new_data[:10], columns=['이름', '나이', '성별', '직업', '사는곳'])
    new_data = new_df.to_dict('records')    
        # person['나이'] -= age_avg
        # new_data.append(person)
        
    return JsonResponse({'new_data': new_data}, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)