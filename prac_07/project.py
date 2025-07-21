class Project:
    """Defines the Project class representing a single project with attributes"""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Construct from given the given values"""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion) #%

    def __repr__(self):
        """Return string"""
        return f"{self.name}, {self.start_date}, {self.priority}, ${self.cost_estimate:.2f}, {self.completion}%"

