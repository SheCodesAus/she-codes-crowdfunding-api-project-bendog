from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_projects")

    def __str__(self):
        return self.title


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="pledges",
    )
    supporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supporter_pledges")


class Comment(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    body = models.TextField()
    visible = models.BooleanField(default=True)
