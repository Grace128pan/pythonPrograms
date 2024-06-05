#without srp, we would like to generate and print report

class Report:
    def __init__(self, title, content):  # Corrected method name
        self.title = title
        self.content = content
        
    def generate(self):
        return f"Title: {self.title}\nContent: {self.content}"
    
    def print_report(self):  # Renamed to avoid conflict with built-in print
        report = self.generate()
        print(report)
        
report = Report("Annual Report", "This is the content of the annual report.")
report.print_report()  # Corrected method call
