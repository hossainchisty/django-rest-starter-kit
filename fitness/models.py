from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    frequency = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    daily_session_duration = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class WorkoutPlanExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    duration = models.IntegerField()
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.workout_plan.name} - {self.exercise.name}"


class Tracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateTimeField()
    fitness_goals = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
