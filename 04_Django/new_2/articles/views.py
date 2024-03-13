from django.shortcuts import render

# Create your views here.
def index(request):
    # app에서 사용할 template은 templates 폴더에 넣는데
    # 왜... app/templates/app/*.html
    # 처럼 app 이름이 중복되도록 폴더 구조를 만들까?
    '''
        만약... templates/*.html 로 만들었다면...
        app이 2개인 경우 articles와 accounts에서
        articles/templates/index.html
        accounts/templates/index.html

        두 파일 중... 순회 순서에 따라 먼저 발견하는 대상
        index.html을 render 하게 되어버린다.

        그러면... 폴더를 그렇게 만들지 말고... 파일명을...
        articles/templates/articles_index.html
        accounts/templates/accounts_index.html

        이렇게 만들면 안되나?
        맞음!
        그러나 근시안적인 시도임

        
    '''
    return render(request, 'articles/index.html')
