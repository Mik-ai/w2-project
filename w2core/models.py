from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    participants = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(blank=True, max_length=100)
    projects_with = models.ManyToManyField(Project, blank=True)
    users_with = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(
        null=True,
        default="",
        blank=True,
        max_length=100,
    )

    # consider using modifiers to make custom statuses for different projects
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    grade = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
