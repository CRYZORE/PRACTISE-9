from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Replacer
from .serializers import ReplacerSerializer
from summary import sum
import summary


class ReplacerView(APIView):

    def get(self, request, s):
        replacer = Replacer(s, summary.summary(s))

        serializer_for_request = ReplacerSerializer(instance=replacer)

        return Response(serializer_for_request.data)

