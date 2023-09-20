
from BasicShanty import BasicShanty
from AdvancedShanty import AdvancedShanty
from MasterShanty import MasterShanty

class MasterBoatswainRiskManagement:
    def __init__(self, trading_capital, risk_tolerance):
        self.trading_capital = trading_capital
        self.risk_tolerance = risk_tolerance
        self.current_positions = {}
        self.current_risk = 0

        # Initialize the different "shanty" levels for risk management
        self.basic_shanty = BasicShanty(self.trading_capital, self.risk_tolerance)
        self.advanced_shanty = AdvancedShanty(self.trading_capital, self.risk_tolerance)
        self.master_shanty = MasterShanty(self.trading_capital, self.risk_tolerance)
        
        # Set the initial shanty level to 'basic'
        self.current_shanty = self.basic_shanty

    # Level up the risk management strategy based on performance metrics
    def level_up(self, performance_metric):
        if performance_metric == 'advanced':
            self.current_shanty = self.advanced_shanty
        elif performance_metric == 'master':
            self.current_shanty = self.master_shanty

    # Evaluate the risk of a proposed trade using the current shanty level
    def evaluate_trade_risk(self, proposed_trade):
        return self.current_shanty.evaluate_trade_risk(proposed_trade)

    # Decide whether to execute a trade based on its evaluated risk
    def decide_trade(self, proposed_trade):
        return self.current_shanty.decide_trade(proposed_trade)

    # Adjust current positions based on new risk evaluations
    def adjust_positions(self):
        self.current_shanty.adjust_positions()
