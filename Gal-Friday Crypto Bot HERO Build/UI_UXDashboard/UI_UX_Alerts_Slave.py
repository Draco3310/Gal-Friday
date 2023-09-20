
class AlertsSlave:
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        """Add a new alert to the system."""
        self.alerts.append(alert)
        # Complexity: O(1), appending to a list

    def get_alerts(self):
        """Fetch all current alerts."""
        return self.alerts
        # Complexity: O(1), simple data retrieval

    def clear_alerts(self):
        """Clear all alerts."""
        self.alerts.clear()
        # Complexity: O(1), clearing a list
