from django.test import TestCase
from api.models import Task

class TaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            title = "Testing Model",
            description = "Test Description",
            complete = False
        )

    def test_task_content(self):
        self.assertEqual(self.task.title, "Test Model")
        self.assertEqual(self.task.complete, False)
    
