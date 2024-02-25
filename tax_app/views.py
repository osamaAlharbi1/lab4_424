from django.http import HttpResponse
from django.shortcuts import render

# Assume a tax rate of 15% (0.15)
TAX_RATE = 0.15

def home(request):
    return HttpResponse("This is a site to calculate tax.")

def calculate_tax(request, number):
    total_cost = number * (1 + TAX_RATE)
    return HttpResponse(f"The total cost including tax is: {total_cost}")

def show_tax_rate(request):
    return render(request, 'tax_rate.html', {'tax_rate': TAX_RATE})
