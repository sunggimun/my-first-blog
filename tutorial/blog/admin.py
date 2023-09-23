from django.contrib import admin
from .models import Post

# Register your models here.
# 관리자 페이지에서 blog 앱에서 만든 Post 모델을 보려면 아래와 같이 등록해 줘야 한다 
admin.site.register(Post)
