from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import TeacherProfile  # обязательно импорт профиля

User = get_user_model()


# Главное меню
def main_menu(request):
    return render(request, 'MainMenu.html')


# Вход в систему
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.role:
                if user.role == 'teacher':
                    return redirect('teacher_dashboard')
                else:
                    return redirect('student_dashboard')
            return redirect('select_role')
        else:
            return render(request, 'Login.html', {'error': 'Неверный логин или пароль'})

    return render(request, 'Login.html')


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'Register.html', {'error': 'Пароли не совпадают'})

        if User.objects.filter(username=username).exists():
            return render(request, 'Register.html', {'error': 'Имя пользователя уже занято'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('main_menu')

    return render(request, 'Register.html')


# Страница курса
def course_view(request):
    return render(request, 'CourseView.html')


# Статические страницы футера
def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def terms_view(request):
    return render(request, 'terms.html')


# Страница выбора роли
def select_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role in ['student', 'teacher']:
            request.user.role = role
            request.user.save()
            if role == 'student':
                return redirect('student_dashboard')
            else:
                return redirect('teacher_dashboard')
    return render(request, 'select_role.html')


# Панель студента
def student_dashboard(request):
    return render(request, 'student_dashboard.html')


# Панель преподавателя
@login_required
def teacher_dashboard(request):
    profile = getattr(request.user, 'teacherprofile', None)
    return render(request, 'teacher_dashboard.html', {'profile': profile})


# Каталог репетиторов
def tutors_view(request):
    return render(request, 'tutors.html')


# Детали курса
def course_detail(request, course_id):
    return render(request, 'course_detail.html', {'course_id': course_id})


# Профиль пользователя (студента или преподавателя)
@login_required
def profile(request):
    user = request.user
    try:
        profile = user.teacherprofile
        nickname = profile.nickname
        bio = profile.bio
        level = profile.level
        about = profile.about
    except:
        nickname = user.username
        bio = ''
        level = 0
        about = ''

    return render(request, 'profile.html', {  # ← просто 'profile.html'
        'nickname': nickname,
        'bio': bio,
        'level': level,
        'about': about,
    })
