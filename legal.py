class LegalConstraints:
    def __init__(self):
        self.warning = """
        ADVANCED SYSTEM MONITORING TOOL - EDUCATIONAL USE ONLY
        
        By using this software, you agree:
        1. This tool will only be used on systems you own or have explicit permission to monitor
        2. You will comply with all applicable laws (Computer Fraud and Abuse Act, GDPR, etc.)
        3. Any data collected will be used solely for educational purposes
        4. You understand unauthorized use may result in legal consequences
        """
        
    def display_and_verify(self):
        print(self.warning)
        response = input("Do you agree to these terms? (yes/no): ").lower()
        if response != 'yes':
            print("Exiting...")
            exit()
        print("Acknowledgement logged. Starting in educational mode.")
