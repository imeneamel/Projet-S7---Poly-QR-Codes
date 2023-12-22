from django.contrib.auth.models import User, Group
from PolyQR.models import Etudiant  

def create_students():
    
    students_group, created = Group.objects.get_or_create(name='Students')

    # Liste des étudiants à créer
    students_data = [
        {'username': 's.smith', 'id': '200', 'firstname': 'Sarah', 'lastname': 'Smith', 'password': 'password6'},
        {'username': 'j.jones', 'id': '201', 'firstname': 'John', 'lastname': 'Jones', 'password': 'password7'},
        {'username': 'e.evans', 'id': '202', 'firstname': 'Emily', 'lastname': 'Evans', 'password': 'password8'},
        {'username': 'm.miller', 'id': '203', 'firstname': 'Michael', 'lastname': 'Miller', 'password': 'password9'},
        {'username': 'a.adams', 'id': '204', 'firstname': 'Alice', 'lastname': 'Adams', 'password': 'password10'},
    ]

    for data in students_data:
        # Créer un utilisateur
        student_user = User.objects.create_user(
            username=data['username'],
            id=data['id'],
            first_name=data['firstname'],
            last_name=data['lastname'],
            password=data['password']
        )

        student_user.groups.add(students_group)

        Etudiant.create(user=student_user)


if __name__ == '__main__':
    create_students()
