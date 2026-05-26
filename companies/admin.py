from django.contrib import admin
from .models import Company, RawRecord

from .models import ESGResult

admin.site.register(ESGResult)

admin.site.register(Company)
admin.site.register(RawRecord)