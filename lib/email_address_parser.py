import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Extract valid email addresses using regex
        emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', self.addresses)
        # Remove duplicates and sort
        return sorted(set(emails))
