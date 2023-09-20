
from strategies import MomentumStrategy, MeanReversionStrategy, MLStrategy  # Assuming these strategies exist

class TradingStrategy:
    def __init__(self):
        self.strategies = {
            'momentum': MomentumStrategy(),
            'mean_reversion': MeanReversionStrategy(),
            'ml': MLStrategy()
        }
        self.default_strategy = MomentumStrategy()
        self.relentless_strategy = MLStrategy()  # Conservative fallback

    def select_strategy(self, market_data, risk_level, jarvis_signal):
        # Evaluate each strategy
        performance_metrics = {}
        for name, strategy in self.strategies.items():
            performance_metrics[name] = strategy.evaluate(market_data, risk_level, jarvis_signal)
        
        # Use 'Relentless' fallback if all strategies underperform
        if all(value <= 0 for value in performance_metrics.values()):
            return self.relentless_strategy

        # Otherwise, select the best performing strategy
        selected_strategy = max(performance_metrics, key=performance_metrics.get)
        return self.strategies.get(selected_strategy, self.default_strategy)
