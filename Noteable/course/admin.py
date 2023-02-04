from django.contrib import admin
from .models import Psychology,Env_science,Human_Geography,World_history,Macroeconomics,US_hisotry

# Register your models here.
admin.site.register(Psychology)
admin.site.register(Macroeconomics)
admin.site.register(Env_science)
admin.site.register(Human_Geography)
admin.site.register(World_history)
admin.site.register(US_hisotry)