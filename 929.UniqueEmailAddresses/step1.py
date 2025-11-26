class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            return f"{local}@{domain}"
        
        seen = {}

        for email in emails:
            normalized = parse(email)
            if normalized not in seen:
                seen[normalized] = True
        return len(seen)
