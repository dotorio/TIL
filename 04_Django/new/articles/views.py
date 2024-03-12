from django.shortcuts import render

# Create your views here.
def index(request):
    # 사용자의 index 페이지 보여 달라는 요청에 적절한 응답은
    # index 페이지 보여주는 것
    return render(request, 'index.html')