from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .forms import InstructionForm
from .models import Instruction


# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, template_name="index.html")


class SearchResultView(ListView):
    model = Instruction
    paginate_by = 3
    template_name = "search/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Instruction.objects.filter(title__icontains=query)
        return object_list


class InstructionListView(ListView):
    model = Instruction
    template_name = "instructions/instructions_list.html"


class InstructionDeleteView(DeleteView):
    model = Instruction
    template_name = "instructions/instruction_delete.html"
    success_url = "/instructions"


class InstructionUpdateView(UpdateView):
    model = Instruction
    fields = ["title", "description"]
    template_name = "instructions/instruction_form.html"
    success_url = "/instructions"


class InstructionDetailView(DetailView):
    model = Instruction
    template_name = "instructions/instruction_detail.html"


class InstructionCreateView(CreateView):
    model = Instruction
    fields = ["title", "description"]
    template_name = "instructions/instruction_form.html"
    success_url = "/instructions"


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
