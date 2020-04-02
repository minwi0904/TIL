practice > 0327 폴더 만들기

0327 폴더 안에서 django-admin startproject intro로 프로젝트 만들기

★필수 cd intro를 통해 '최상위폴더'로 들어가기

python manage.py startapp pages 로 앱 생성

그러고 난 후 intro/intro에 있는 settings로 들어가서 

```
1) ALLOWED_HOSTS에 별을 추가 ex) '*'

2) INSTALLED_APPS 에 앱을 추가한다 ex) 'pages',
```

pages안에 잇는 views를 가져와야하므로

```
intro > urls에서 from pages import views
    urls 속에 있는urlpatterns에  path('dinner/<str:menu>/<int:people>/', views.dinner), 작성
```

그리고 views에 들어가서 함수를 작성한다.

예시 )

```
from django.shortcuts import render

# Create your views here.
def dinner(request, menu, people):
    context ={
        'menu':menu,
        'people':people,
    }
    return render(request, 'dinner.html',context)
```

그러고 난 후 pages 안에 templates 폴더를 만들고 (django기 때문에)
그 밑에 dinner.html을 생성한다.

그러고 난 후 dinner.html에 화면에 표시할 것들을 작성한다.
예시 )

```
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>저녁메뉴</h1>
    <h1>저녁 먹을 사람?! {{ people }}</h1>
    <h1>어떤 메뉴?! {{ menu }}</h1>
</body>
</html>
이런 식으로 작성한다.
```

그리고 난 후에 ''최상위 폴더''에서 `python manage.py runserver 8080` 를 실행한다.
그리고 `page not found`가 떳을때 뒤에 `dinner/3/hamberger`를 추가시키고 F5