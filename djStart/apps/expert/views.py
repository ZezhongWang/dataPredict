from django.shortcuts import render
from django.views.generic.base import View
from apps.expert.forms import ExpertForm, ResetForm
from apps.expert.models import Expert
from apps.message.models import UserProfile
from apps.message.views import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


class MainInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "main_info.html")


class MainResetView(LoginRequiredMixin, View):
    def get(self, request):
        hash_key = CaptchaStore.generate_key()
        image_url = captcha_image_url(hash_key)
        return render(request, "main_reset.html", {"hash_key": hash_key, "image_url": image_url})

    def post(self, request):
        reset_form = ResetForm(request.POST)
        username = request.user.username
        password = request.POST.get("password_before", "")
        user = authenticate(username=username, password=password, type="expert")
        if user is None:
            hash_key = CaptchaStore.generate_key()
            image_url = captcha_image_url(hash_key)
            return render(request, "main_reset.html", {"hash_key": hash_key, "image_url": image_url,
                                                       "msg": "用户密码错误！"})
        if reset_form.is_valid():
            username = request.user.username
            password = request.POST.get("password_after", "")
            user = UserProfile.objects.get(username=username)
            user.password = make_password(password)
            user.save()
            login(request, user)
            response = HttpResponse()
            response.write("<script> alert('修改密码成功'); location='/main/';</script>")
            return response
        else:
            hash_key = CaptchaStore.generate_key()
            image_url = captcha_image_url(hash_key)
            return render(request, "main_reset.html", {"hash_key": hash_key, "image_url": image_url,
                                                       "reset_form": reset_form})


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            username = request.user.username
            expert = Expert.objects.get(username=username)
        except Expert.DoesNotExist:
            return render(request, "main.html")
        else:
            return render(request, "main.html", {"expert": expert})

    def post(self, request):
        # 获取帐号对应的Expert
        username = request.user.username
        try:
            expert = Expert.objects.get(username=username)
        except Expert.DoesNotExist:
            expert = Expert(username=username)
        # form
        expert_form = ExpertForm(request.POST, request.FILES, instance=expert)
        if expert_form.is_valid():
            expert.state = 'done'
            expert_form.state = 'done'
            expert_form.save()
            # login(request, request.user)
            # response = HttpResponse()
            # response.write("<script> alert('修改密码成功'); location='/main/';</script>")
            return HttpResponseRedirect("/main/info/")
        else:
            response = HttpResponse()
            response.write("<script> history.go(-1); </script>")
            return response
            # return render(request, "main.html", {"expert_form": expert_form})



