from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def suma(request, op1, op2):
    return HttpResponse('<h1>Sumar:</h1>' + op1 + '+'+ op2 + '=' + str(int(op1) + int(op2)))

def resta(request, op1, op2):
    return HttpResponse('<h1>Restar:</h1>' + op1 + '-'+ op2 + '=' + str(int(op1) - int(op2)))

def multiplica(request, op1, op2):
    return HttpResponse('<h1>Multiplicar:</h1>' + op1 + '*'+ op2 + '=' + str(int(op1) * int(op2)))

def divide(request, op1, op2):
    return HttpResponse('<h1>Dividir:</h1>' + op1 + '/'+ op2 + '=' + str(int(op1) / int(op2)))
