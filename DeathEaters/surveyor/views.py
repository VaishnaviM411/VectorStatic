from django.shortcuts import render

# Create your views here.
class houselisting(View):
    def get(self, request):
        return render(request, 'houselisting.html')
    
class households(View):
    def get(self, request):
        return render(request, 'households.html')