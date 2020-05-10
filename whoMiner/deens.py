import dns
import re
import dns.resolver


class Resolver:
    """
    """

    _cleanDomain=re.compile(r"http[s]?\:\/\/", re.I)

    @classmethod
    def query(cls, domain, queryType):
        """
        """
        try:
            ans=dns.resolver.query(domain, queryType)
            for a in ans:yield a
        except dns.exception.DNSException:
            yield None

    def __init__(self, domain):
        """
        """
        self._rawDomain=domain
        self._domain=self._cleanDomain.sub("", domain)

    def __getattr__(self, attr):
        """
        """
        if attr not in {"A","NS","MX","TXT", "SOA"}:
            raise AttributeError("[-] Unkown attribute")
        try:
            return self.__getattribute__(attr)
        except AttributeError:
            genis=self.query(self._domain, attr)
            data=[rdata.to_text() for rdata in genis if rdata]
            setattr(self, attr, data)
            return self.__getattribute__(attr)
