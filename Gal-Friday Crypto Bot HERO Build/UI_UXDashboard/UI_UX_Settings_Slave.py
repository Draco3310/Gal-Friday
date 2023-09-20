
class SettingsSlave:
    def __init__(self):
        self.settings = {}

    def update_settings(self, new_settings):
        """Update the system settings."""
        self.settings.update(new_settings)
        # Update the system based on the new settings
        # Complexity: O(n), where n is the number of settings to update

    def get_settings(self):
        """Fetch the current settings."""
        return self.settings
        # Complexity: O(1), simple data retrieval

    def reset_settings(self):
        """Reset settings to their default values."""
        self.settings.clear()
        # Complexity: O(1), clearing a dictionary
