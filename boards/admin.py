from django.contrib import admin

# Register your models here.
from .models import Board
from .models import Topic
from .models import Post
from .models import ComapnySchedule
from .models import CompanyCriteriaAndOffer
from .models import CompanyTable


admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(CompanyTable)
admin.site.register(ComapnySchedule)
admin.site.register(CompanyCriteriaAndOffer)

