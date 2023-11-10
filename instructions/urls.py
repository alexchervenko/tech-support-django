from django.urls import path

from .views import (
    Index,
    InstructionCreateView,
    InstructionDetailView,
    InstructionUpdateView,
    InstructionDeleteView,
    SearchResultView,
)

urlpatterns = [
    path("", Index.as_view(), name="main_page"),
    path("search", SearchResultView.as_view(), name="search_results"),
    path("create", InstructionCreateView.as_view()),
    path(
        "detail/<int:pk>/", InstructionDetailView.as_view(), name="instruction_detail"
    ),
    path("update/<int:pk>/", InstructionUpdateView.as_view(), name="edit_page"),
    path("delete/<int:pk>/", InstructionDeleteView.as_view(), name="delete_page"),
]
