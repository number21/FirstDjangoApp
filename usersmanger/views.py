from django.shortcuts import render

# Create your views here.
def get_fb_user(request):
    # if request.user.is_authenticated():
    try:
        user_fb = UserSocialAuth.objects.get(user=request.user.id)
    except UserSocialAuth.DoesNotExist:
        user_fb = None
    return user_fb


def login_page(request):
    return render(request, 'registration/templates/registration/login.html')
