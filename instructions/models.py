from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(help_text="The name of the category", max_length=50)

    def __str__(self):
        return f"{self.title}"


class Instruction(models.Model):
    title = models.CharField(max_length=100, help_text="The name of the problem")
    description = models.TextField(
        help_text="Description of the problem", max_length=1000
    )
    category = models.ForeignKey(
        Category,
        help_text="Category of the problem",
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.title}"
