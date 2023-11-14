from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import InstructionForm
from .models import Instruction


# Create your views here.


class Index(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, template_name="index.html")


class SearchResultView(LoginRequiredMixin, ListView):
    model = Instruction
    paginate_by = 10
    template_name = "search/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Instruction.objects.filter(title__icontains=query).order_by("-id")
        return object_list


class InstructionCreateView(LoginRequiredMixin, CreateView):
    model = Instruction
    fields = ["title", "description"]
    template_name = "instructions/instruction_form.html"
    success_url = "/instructions"


class InstructionDetailView(LoginRequiredMixin, DetailView):
    model = Instruction
    template_name = "instructions/instruction_detail.html"


class InstructionUpdateView(LoginRequiredMixin, UpdateView):
    model = Instruction
    fields = ["title", "description"]
    template_name = "instructions/instruction_form.html"
    success_url = "/instructions"


class InstructionDeleteView(LoginRequiredMixin, DeleteView):
    model = Instruction
    template_name = "instructions/instruction_delete.html"
    success_url = "/instructions"
