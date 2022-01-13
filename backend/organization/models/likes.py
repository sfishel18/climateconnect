from django.db import models
from organization.models.project import Project
from organization.models.content import Post
from django.contrib.auth.models import User

class Like(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="project_liked",
        verbose_name="Project",
        help_text="Points to a project",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    post = models.ForeignKey(
        Post,
        related_name="post_liked",
        verbose_name="Post",
        help_text="Points to a post",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        User,
        related_name="liking_user",
        verbose_name="Liking User",
        help_text="Points to the user who liked the project",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        help_text="Time when the user liked the project",
        verbose_name="Created At",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        help_text="Time when the like was updated",
        verbose_name="Updated At",
        auto_now_add=True
    )

    class Meta:
        app_label = "organization"
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ["-id"]

    def __str__(self):
        return "%s liked %s " % (self.user, self.project.name)