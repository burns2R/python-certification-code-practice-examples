class UserActivity:
    def __init__(self, user_id):
        self.user_id = user_id
        self.activity = []
        self.record = {}

    def add_activity(self, timestamp, action):

        self.record['timestamp'] = timestamp
        self.record['action'] = action
        self.activity.append(self.record)

# Note: Just need to initiate the class instance for user_id 123.
# Proof: https://docs.python.org/3/tutorial/classes.html#method-objects 
user_activity = UserActivity(123)

# Add a row of activity to the instance
user_activity.add_activity('2022-03-19 10:00:00', 'login')

print('UserActivity:', 'user_id:', user_activity.user_id, 'activity:', user_activity.activity)