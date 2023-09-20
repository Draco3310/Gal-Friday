
class MasterHeimdallAlerts:
    def __init__(self):
        self.slaves = []
        self.alert_log = []

    def register_slave(self, slave):
        self.slaves.append(slave)
    
    def collect_alerts(self):
        for slave in self.slaves:
            alert = slave.generate_alert()
            if alert:
                self.alert_log.append(alert)
                self.dispatch_alert(alert)

    def dispatch_alert(self, alert):
        print(f"Dispatching alert: {alert}")
    