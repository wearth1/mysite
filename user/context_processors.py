from .forms import LoginForm


def login_medal_form(request):
    return {'login_medal_form': LoginForm()}