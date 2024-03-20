from django.core.management.base import BaseCommand
from fitness.models import Exercise, WorkoutPlan, WorkoutPlanExercise, Tracking
from django.contrib.auth.models import User
from django.utils import timezone
from random import randint, choice


class Command(BaseCommand):
    help = "Populate predefined data into the database"

    def handle(self, *args, **options):
        # Seed exercises
        exercises = [
            {
                "name": "Push-up",
                "description": "Push-up is a common bodyweight exercise that works the muscles of the upper body.",
                "instructions": "Start in a plank position with hands shoulder-width apart. Lower your body until your chest nearly touches the floor. Push back up to the starting position.",
                "target_muscles": "Chest, shoulders, triceps",
            },
            {
                "name": "Squats",
                "description": "Squats are a compound exercise that targets the muscles of the lower body.",
                "instructions": "Stand with feet shoulder-width apart. Bend your knees and lower your body as if you are sitting back into a chair. Keep your chest up and back straight. Push through your heels to return to the starting position.",
                "target_muscles": "Quadriceps, hamstrings, glutes",
            },
            # Add more exercises here
        ]

        for exercise_data in exercises:
            exercise = Exercise.objects.create(**exercise_data)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created exercise: {exercise.name}")
            )

        # Seed users
        for i in range(5):  # Create 5 users for testing
            username = f"user{i}"
            print(username)
            email = f"user{i}@example.com"
            password = "password"  # Change this if needed
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created user: {user.username}")
            )

        # Seed workout plans
        users = User.objects.all()
        for user in users:
            plan = WorkoutPlan.objects.create(
                user=user,
                name=f"{user.username}'s Workout Plan",
                description="Custom workout plan",
                frequency="3 days per week",
                goal="Build muscle",
                daily_session_duration=60,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created workout plan for user: {user.username}"
                )
            )

        # Seed workout plan exercises
        workout_plans = WorkoutPlan.objects.all()
        for plan in workout_plans:
            for i in range(3):  # Add 3 exercises to each plan
                exercise = Exercise.objects.order_by(
                    "?"
                ).first()  # Randomly select an exercise
                repetitions = randint(8, 12)  # Random repetitions between 8 and 12
                sets = randint(3, 5)  # Random sets between 3 and 5
                if (
                    exercise.name == "Running"
                ):  # If the exercise is Running, set distance
                    distance = randint(1, 5)  # Random distance between 1 and 5 miles
                    duration = None
                else:  # For other exercises, set duration
                    duration = randint(
                        20, 45
                    )  # Random duration between 20 and 45 minutes
                    distance = None
                WorkoutPlanExercise.objects.create(
                    workout_plan=plan,
                    exercise=exercise,
                    repetitions=repetitions,
                    sets=sets,
                    duration=duration,
                    distance=distance,
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added exercise to workout plan: {exercise.name}"
                    )
                )

        # Seed tracking data
        for user in users:
            for i in range(10):  # Add 10 tracking entries for each user
                weight = randint(60, 100)  # Random weight between 60 and 100 kg
                date = timezone.now() - timezone.timedelta(
                    days=i
                )  # Date in the past 10 days
                fitness_goals = (
                    "Lose weight" if i % 2 == 0 else "Gain muscle"
                )  # Alternate goals
                Tracking.objects.create(
                    user=user, weight=weight, date=date, fitness_goals=fitness_goals
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added tracking data for user: {user.username}"
                    )
                )
