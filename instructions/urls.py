from django.urls import path
from .views import (
    Index,
    InstructionRecordFormView,
    FormSuccessView,
    DeleteSuccessView,
    InstructionCreateView,
    InstructionDetailView,
    InstructionUpdateView,
    InstructionDeleteView,
    InstructionListView,
)

urlpatterns = [
    path("", Index.as_view()),
    path("new_instruction", InstructionRecordFormView.as_view()),
    path("entry_success", FormSuccessView.as_view()),
    path("delete_success", DeleteSuccessView.as_view()),
    path("create", InstructionCreateView.as_view()),
    path(
        "detail/<int:pk>/",
        InstructionDetailView.as_view(),
        name="instruction_detail",
    ),
    path("update/<int:pk>/", InstructionUpdateView.as_view()),
    path("delete/<int:pk>/", InstructionDeleteView.as_view()),
    path("list", InstructionListView.as_view()),
]
