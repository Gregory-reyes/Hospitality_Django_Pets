from django.contrib import admin
from .models.usuario import Usuario
from .models.signos_vitales import Signos_vitales
from .models.paciente import Paciente
from .models.personal_de_salud import Personal_salud
from .models.familiar import Familiar
from .models.historia_clinica import Historia_clinica

admin.site.register(Usuario)
admin.site.register(Signos_vitales)
admin.site.register(Paciente)
admin.site.register(Personal_salud)
admin.site.register(Familiar)
admin.site.register(Historia_clinica)