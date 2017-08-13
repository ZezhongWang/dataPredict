from django.shortcuts import render
from django.views.generic.base import View
from apps.expert.forms import ExpertForm
from apps.expert.models import Expert
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, "main.html", {})

    def post(self, request):
        expert_form = ExpertForm(request.POST)
        if expert_form.is_valid():
            expert_number = request.POST.get("expert_number", "")
            gender = request.POST.get("gender", "")
            valid_time = request.POST.get("valid_time", "")
            expert = Expert()
            expert.expert_number = expert_number
            expert.gender = gender
            expert.valid_time = valid_time
            expert.save()
            response = HttpResponse()
            response.write("<script> alert('注册成功'); location('/main/'); </script>")
            return response
        else:
            return render(request, "main.html", {"expert_form": expert_form})