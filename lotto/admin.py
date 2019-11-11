from django.contrib import admin
from lotto.models import GuessNumbers  # 같은 폴더 경로이기에 lotto 생략 가능

# Register your models here.
admin.site.register(GuessNumbers)
