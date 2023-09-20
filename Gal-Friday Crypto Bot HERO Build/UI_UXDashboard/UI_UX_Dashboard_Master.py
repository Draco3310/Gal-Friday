
# UI_UX_Dashboard_Master.py

from UI_UX_Dashboard_Slave import UIDashboardSlave
from UI_UX_Settings_Slave import UISettingsSlave
from UI_UX_Alerts_Slave import UIAlertsSlave

class UIDashboardMaster:
    def __init__(self):
        # Initialize the slave components
        self.dashboard_slave = UIDashboardSlave()
        self.settings_slave = UISettingsSlave()
        self.alerts_slave = UIAlertsSlave()

    def render_dashboard(self):
        # Render the dashboard UI
        self.dashboard_slave.render()

    def update_settings(self, new_settings):
        # Update the settings UI with new values
        self.settings_slave.update(new_settings)

    def alert_handler(self, alert_type, message):
        # Handle alerts and notifications
        self.alerts_slave.handle(alert_type, message)

# Create an instance of the master class
ui_master = UIDashboardMaster()

# Example usage
ui_master.render_dashboard()
ui_master.update_settings({"theme": "dark", "notifications": True})
ui_master.alert_handler("warning", "Market volatility detected.")
