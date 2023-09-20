
import logging
from DataProcessingSlave import DataProcessingSlave
from RiskManagementSlave import RiskManagementSlave
from TradingStrategySlave import TradingStrategySlave
from TradingExecutorSlave import TradingExecutorSlave
from NotificationAlertsSlave import NotificationAlertsSlave
from UI_UX_DashboardSlave import UI_UX_DashboardSlave

class MainControllerMaster:
    def __init__(self):
        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        logging.info("Initializing Main Controller Master")

        # Initialize Slave modules
        self.data_processing_slave = DataProcessingSlave()
        self.risk_management_slave = RiskManagementSlave()
        self.trading_strategy_slave = TradingStrategySlave()
        self.trading_executor_slave = TradingExecutorSlave()
        self.notification_alerts_slave = NotificationAlertsSlave()
        self.ui_ux_dashboard_slave = UI_UX_DashboardSlave()

    def start(self):
        # Main function to start the trading bot
        logging.info("Starting the trading bot")

        # Fetch the raw data
        raw_data = self.data_processing_slave.fetch_raw_data()
        
        # Transform the data
        transformed_data = self.data_processing_slave.transform_data(raw_data)
        
        # Perform risk assessment
        is_risk_acceptable = self.risk_management_slave.assess_risk(transformed_data)
        
        if is_risk_acceptable:
            # Generate trading signal
            trading_signal = self.trading_strategy_slave.generate_trading_signal(transformed_data)
            
            # Execute the trade
            self.trading_executor_slave.execute_trade(trading_signal)
            
            # Send the notification
            self.notification_alerts_slave.send_notification(trading_signal)
            
            # Update the UI
            self.ui_ux_dashboard_slave.update_ui(transformed_data, trading_signal)
        else:
            logging.warning("Risk assessment failed. No trading signal generated.")
