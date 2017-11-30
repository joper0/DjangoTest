# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from demo.helpers.date_helper import DateHelper
# Create your views here.

# Vista basada en clases


class HourList(APIView):
    # Es importante modularizar el proyecto,las funciones que usaremos comunmente
    # tenerlos en helpers o funciones globales
    def get(self, request, format=None):
        return JsonResponse({'hora_actual': DateHelper().get_date_now()}, status=200)
