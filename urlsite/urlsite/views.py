from django.http import HttpResponse

def main_page(request):
    return HttpResponse("main page")

def product(request, id=1, color='black'):
    resp = f'Product id: {id}, color: {color}'
    return HttpResponse(resp)

def product_amount(request, id, amount):
    resp = f'Product id: {id}, amount: {amount}'
    return HttpResponse(resp)

def category(request, lang):
    resp = f'language: {lang}'
    return HttpResponse(resp)