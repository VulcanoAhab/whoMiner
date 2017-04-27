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
        if attr not in {"A","NS","MX","TXT"}:
            raise AttributeError("[-] Unkown attribute")
        try:
            return self.__getattribute__(attr)
        except AttributeError:
            setattr(self, attr, list(self.query(self._domain, attr)))
            return self.__getattribute__(attr)
