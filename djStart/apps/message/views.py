from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile
from apps.expert.models import Expert
from .forms import LoginForms, RegisterForms
from django.db.models import Q
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, type="expert"):
        try:
            user = UserProfile.objects.get(Q(username=username), Q(type=type))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):

    def get(self, request):
        hash_key = CaptchaStore.generate_key()
        image_url = captcha_image_url(hash_key)
        return render(request, 'message_register.html', {"hash_key": hash_key, "image_url": image_url})

    def post(self, request):
        register_form = RegisterForms(request.POST)
        if register_form.is_valid():
            account = request.POST.get("account", "")
            password = request.POST.get("password", "")
            try:
                UserProfile.objects.get(Q(username=account), Q(type="expert"))
            except UserProfile.DoesNotExist:
                # 没有相同用户
                user = UserProfile()
                user.username = account
                user.password = make_password(password)
                user.save()
                expert = Expert(username=user)
                expert.save()
                response = HttpResponse()
                response.write("<script> alert('注册成功'); location='/login/';</script>")
                return response
            else:
                hash_key = CaptchaStore.generate_key()
                image_url = captcha_image_url(hash_key)
                return render(request, 'message_register.html', {"hash_key": hash_key, "image_url": image_url,
                                                                 "msg": "该用户名已存在"})

        else:
            hash_key = CaptchaStore.generate_key()
            image_url = captcha_image_url(hash_key)
            return render(request, 'message_register.html', {"hash_key": hash_key, "image_url": image_url,
                                                             "register_form": register_form})


class LoginView(View):
    def get(self, request):
        hash_key = CaptchaStore.generate_key()
        image_url = captcha_image_url(hash_key)
        return render(request, 'message_login.html', {"hash_key": hash_key, "image_url": image_url})

    def post(self, request):
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            account = request.POST.get("account", "error")
            password = request.POST.get("password", "error")
            type = request.POST.get("type")
            user = authenticate(username=account, password=password, type=type)
            if user is not None:
                if type == 'expert':
                    login(request, user)
                    # response = HttpResponse()
                    # response.write("<script> alert('登录成功'); location='/main/';</script>")
                    return HttpResponseRedirect('/main/')
                else:
                    return HttpResponseRedirect('/admin/')
            else:
                return render(request, "message_login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "message_login.html", {"login_form": login_form})

        # # 登录阶段
        # login_form = LoginForms(request.POST)
        # if login_form.is_valid():
        #     user_id = request.POST.get('account', "error")
        #     password = request.POST.get('password', "error")
        #     type = request.POST.get('type', "error")
        #     try:
        #         login_user = User.objects.get(Q(user_id=user_id), Q(type=type))
        #     except User.DoesNotExist:
        #         # 用户不存在
        #         return render(request, 'message_login.html', {"msg": "用户名或密码错误"})
        #     else:
        #         if password == login_user.password:
        #             return render(request, 'login2.html')
        # else:
        #     return render(request, 'message_login.html', {"login_form": login_form})


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


