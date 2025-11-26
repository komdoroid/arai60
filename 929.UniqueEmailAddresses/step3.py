class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            return f"{local}@{domain}"

        normalized_emails = {normalize(email) for email in emails}
        return len(normalized_emails)      
