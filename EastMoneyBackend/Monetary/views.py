# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Monetary
from .serializers import MonetarySerializer

from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination

import json
# Create your views here.


class MyPageNumberPagination(PageNumberPagination):

    page_size = 2  
    page_size_query_param = 'size'  
    max_page_size = 1000  
    page_query_param = 'page'  



class MonetaryViewSet(viewsets.ModelViewSet):

    queryset = Monetary.objects.all()
    serializer_class = MonetarySerializer

    def get_queryset(self):
        total_monetary_fund = Monetary.objects.all()     
        print("asdsa")  
        return total_monetary_fund

    def create(self, request, *args, **kwargs):
        serializer = MonetarySerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

