import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from users.models import User


def create_superuser():
    username = 'richar01'
    email = 'ricardoproblaz@gmail.com'
    password = 'DJANGOsoocerr35'

#      username = 'richar01'                                                                                                         │
#  │   email = 'ricardoproblaz@gmail.com'                                                                                            │
#  │   password = 'DJANGOsoocerr35'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f'Superuser {username} created successfully!')
    else:
        print(f'Superuser {username} already exists.')


if __name__ == '__main__':
    create_superuser()
