from datetime import datetime


class Project:
    """Defines the Project class representing a single project with attributes"""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Construct from given the given values"""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion) #%

    def __str__(self):
        try:
            date_object = datetime.strptime(self.start_date, "%Y-%m-%d")
            formatted = date_object.strftime("%a %d %b %Y")
        except ValueError:
            formatted = self.start_date

        return f"{self.name}, {formatted}, Priority: {self.priority}, Cost: ${self.cost_estimate:.2f}, Complete: {self.completion}%"

    def is_complete(self):
        return self.completion == 100

    def is_not_complete(self):
        return self.completion < 100