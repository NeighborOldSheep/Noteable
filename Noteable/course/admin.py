from django.contrib import admin
from .models import Psychology,Economics,Env_science,Human_Geography,World_history,Seminar

# Register your models here.
admin.site.register(Psychology)
admin.site.register(Economics)
admin.site.register(Env_science)
admin.site.register(Human_Geography)
admin.site.register(World_history)
admin.site.register(Seminar)