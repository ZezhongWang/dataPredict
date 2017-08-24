from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.models import Q
from apps.expert.models import Expert
from apps.message.views import LoginRequiredMixin
# Create your views here.


class AdminView(LoginRequiredMixin, View):
    def get(self, request):

        all_expert = Expert.objects.filter(Q(state='done') | Q(state='checked') | Q(state='denied'))
        number = all_expert.count()
        return render(request, 'admin.html', {'number': number})


class ListView(LoginRequiredMixin, View):
    def get(self, request):
        all_expert = Expert.objects.filter(Q(state='done') | Q(state='checked') | Q(state='denied'))
        state = request.GET.get('state', "")
        if state != "all" and state != "":
            all_expert = all_expert.filter(Q(state=state))
        return render(request, 'admin_list.html', {"all_expert": all_expert})


class DetailView(LoginRequiredMixin, View):
    def get(self, request, username):
        expert = get_object_or_404(Expert, username=username)
        return render(request, 'admin_detail.html', {'expert': expert})

    def post(self, request, username):
        expert = get_object_or_404(Expert, username=username)
        expert.expert_number = request.POST.get("expert_number", "")
        expert.valid_time = request.POST.get("valid_time", "")
        if request.POST.get("Action") == "checked":
            expert.state = "checked"
        else:
            expert.state = "denied"
        expert.save()
        return render(request, 'admin_detail.html', {'expert': expert})
