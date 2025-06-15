class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        myset = set();
        for email in emails:
            # local,domain = email.split("@");
            # local = local.split("+")[0];
            # local = local.replace(".","");
            # myset.add((local,domain));
            i=0;
            local = "";
            while email[i] not in "@+":
                if email[i] != ".":
                    local =local+email[i];
                i=i+1;
            while email[i]!="@":
                i=i+1;
            domain = email[i+1:];
            myset.add((local,domain));
        return len(myset);

