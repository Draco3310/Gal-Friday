
class DashboardSlave:
    def __init__(self):
        self.dashboard_data = {}

    def update_dashboard(self, data):
        """Update the data displayed on the dashboard."""
        self.dashboard_data.update(data)
        # Update the UI with the new data
        # Complexity: O(n), where n is the number of data points to update

    def get_dashboard_data(self):
        """Fetch the current dashboard data."""
        return self.dashboard_data
        # Complexity: O(1), simple data retrieval

    def reset_dashboard(self):
        """Reset the dashboard to its initial state."""
        self.dashboard_data.clear()
        # Complexity: O(1), clearing a dictionary
