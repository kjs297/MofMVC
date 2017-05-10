from django.shortcuts import render

def post_list(request):
    return render(request, 'modelapp/post_list.html')