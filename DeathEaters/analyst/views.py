from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
def isAnalyst(group_name):
    if group_name == 'analyst_group':
        return 1
    else:
        return 0


class analystPage(View):
    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            return render(request, 'analystPage.html')
        except:
            return render(request, 'login.html')

class houseHoldQueries(View):
    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            return render(request, 'houseHoldQueries.html')
        except:
            return render(request, 'login.html')

class houseListQueries(View):
    def get(self, request):
        try:
            group = request.user.groups.all()[0].name
            if isAnalyst(group) == 0:
                return render(request, 'login.html')
            return render(request, 'houseListQueries.html')
        except:
            return render(request, 'login.html')