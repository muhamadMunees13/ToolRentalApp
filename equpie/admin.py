from django.contrib import admin

from .models import login
admin.site.register(login)

from .models import products
admin.site.register(products)

from .models import prent
admin.site.register(prent)

from .models import lrent
admin.site.register(lrent)