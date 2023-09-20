
from TradingStrategySelectorSlave import TradingStrategy
from RiskManagement import RiskManagement  # Assuming a RiskManagement module exists
from JarvisPredictiveAnalysis import JarvisPredictiveAnalysis  # Assuming the JARVIS module exists

class TradingStrategySelectorMaster:
    def __init__(self):
        self.trading_strategy = TradingStrategy()
        self.risk_management = RiskManagement()
        self.jarvis = JarvisPredictiveAnalysis()

    def select_trading_strategy(self, market_data, risk_parameters):
        jarvis_signal = self.jarvis.get_signal(market_data)
        risk_level = self.risk_management.get_current_risk_level(risk_parameters)
        
        selected_strategy = self.trading_strategy.select_strategy(market_data, risk_level, jarvis_signal)
        return selected_strategy
