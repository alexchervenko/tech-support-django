from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Instruction
from .forms import InstructionForm


# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, template_name="instructions/index.html")


class InstructionListView(ListView):
    model = Instruction
    template_name = "instructions/instructions_list.html"
    success_url = "/instructions/delete_success"


class InstructionDeleteView(DeleteView):
    model = Instruction
    template_name = "instructions/instruction_delete.html"
    success_url = "/instructions/delete_success"


class InstructionUpdateView(UpdateView):
    model = Instruction
    fields = ["title", "description"]
    template_name = "instructions/instruction_form.html"
    success_url = "/instructions/entry_success"


class InstructionDetailView(DetailView):
    model = Instruction
    template_name = "instructions/instruction_detail.html"


class InstructionCreateView(CreateView):
    model = Instruction
    fields = ["title", "description"]
    template_name = "instructions/instruction_form.html"
    success_url = "/instructions/entry_success"


class InstructionRecordFormView(FormView):
    template_name = "instruction_form.html"
    form_class = InstructionForm
    success_url = "/instructions/entry_success"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Instruction saved successfully")


class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Instruction deleted successfully")
