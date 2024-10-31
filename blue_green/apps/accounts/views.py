from django.shortcuts import render
from blue_green.apps.accounts.models import User

def user_list(request):
    users = User.objects.all()  # Obter todos os usuários
    return render(request, 'accounts/user_list.html', {'users': users})
