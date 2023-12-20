from django.contrib import admin
from .models import Admin, Professeur, Etudiant, Promotion, SalleDeClasse, Cours, Matiere, PresenceEtudiant

admin.site.register(Admin)
admin.site.register(Professeur)
admin.site.register(Etudiant)
admin.site.register(Promotion)
admin.site.register(SalleDeClasse)
admin.site.register(Cours)
admin.site.register(Matiere)
admin.site.register(PresenceEtudiant)
