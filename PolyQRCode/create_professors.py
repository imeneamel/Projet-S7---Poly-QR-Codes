from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from PolyQR.models import Professeur  # Importez le modèle Professeur depuis votre application

def create_professors():
    # Créez un groupe pour les professeurs s'il n'existe pas
    professors_group, created = Group.objects.get_or_create(name='Professors')

    # Ajoutez des permissions spécifiques pour les professeurs
    content_type = ContentType.objects.get_for_model(User)  # Vous pouvez ajuster cela en fonction de vos modèles

    # Vérifiez si la permission existe déjà
    permission, created = Permission.objects.get_or_create(
        codename='can_change_attendance',  # Remplacez par le codename de la permission nécessaire
        content_type=content_type,
        defaults={'name': 'Can Change Attendance'}
    )

    # Liste des professeurs à créer
    professors_data = [
        {'username': 'professor1', 'password': 'password1'},
        {'username': 'professor2', 'password': 'password2'},
        # Ajoutez d'autres professeurs selon vos besoins
    ]

    for data in professors_data:
        # Créez un utilisateur
        professor_user = User.objects.create_user(data['username'], password=data['password'])

        # Ajoutez l'utilisateur au groupe des professeurs
        professor_user.groups.add(professors_group)

        # Ajoutez des privilèges spécifiques
        professor_user.user_permissions.add(permission)

        # Créez une instance du modèle Professeur associée à cet utilisateur
        Professeur.objects.create(user=professor_user)

        # Ajoutez d'autres attributions de rôles ou de permissions selon vos besoins

if __name__ == '__main__':
    create_professors()