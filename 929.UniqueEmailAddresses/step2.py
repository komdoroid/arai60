class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_to_seen = {}
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', "")
            normalized = local + '@' + domain
            normalized_to_seen[normalized] = True

        return len(normalized_to_seen)            
