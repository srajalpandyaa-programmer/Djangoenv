from django.shortcuts import render
from .models import Student

# Create your views here.
def portfolio(request):
    students = Student.objects.all()
    return render(request, 'portfolio/portfolio.html', {'students': students})
