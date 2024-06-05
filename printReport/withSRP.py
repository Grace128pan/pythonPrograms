#with SRP(single responsibility principle)

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
    def generate(self):
        return f"Title: {self.title}\nContent: {self.content}"
    
class ReportPrinter:
    def print_report(self, report):
        print(report.generate())
        
        
report = Report("Annual Report", "This is the content of the annual report.")
printer = ReportPrinter()
printer.print_report(report)