from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from PolyQR.models import Professeur  
def create_professors():
    # Créer un groupe pour les professeurs s'il n'existe pas
    professors_group, created = Group.objects.get_or_create(name='Professors')

    # Ajoutez des permissions spécifiques pour les professeurs
    content_type = ContentType.objects.get_for_model(User)  # Vous pouvez ajuster cela en fonction de vos modèles

    # Vérifier si la permission existe déjà
    permission, created = Permission.objects.get_or_create(
        codename='can_change_attendance',  # Remplacez par le codename de la permission nécessaire
        content_type=content_type,
        defaults={'name': 'Can Change Attendance'}
    )

    # Liste des professeurs à créer
    professors_data = [
        {'username': 'a.poulain', 'id': '123', 'firstname': 'Amélie', 'lastname': 'Poulain', 'password': 'password1'},
        {'username': 'p.dupont', 'id': '124', 'firstname': 'Paul', 'lastname': 'Dupont', 'password': 'password2'},
        {'username': 'm.dubois', 'id': '125', 'firstname': 'Marie', 'lastname': 'Dubois', 'password': 'password3'},
        {'username': 'j.martin', 'id': '126', 'firstname': 'Jean', 'lastname': 'Martin', 'password': 'password4'},
        {'username': 'l.bernard', 'id': '127', 'firstname': 'Lucie', 'lastname': 'Bernard', 'password': 'password5'},
    ]

    for data in professors_data:
        # Créez un utilisateur
        professor_user = User.objects.create_user(data['username'], password=data['password'])

        professor_user.groups.add(professors_group)

        professor_user.user_permissions.add(permission)

        Professeur.create(user=professor_user)

if __name__ == '__main__':
    create_professors()