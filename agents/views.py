from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm

# Create your views here.

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self,form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.UserProfile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
