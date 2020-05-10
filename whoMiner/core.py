from whoMiner.deens import Resolver
from whoMiner.aipees import BasicIPWho

class EnrichDomain:
    """
    """
    def __init__(self, domain):
        """
        """
        self.domain=domain
        self._response={
            "domain":self.domain,
            "dns":{},
            "ipWho":{}
            }
        self._run()

    def _DNS(self):
        """
        """
        _dns=Resolver(self.domain)
        self._response["dns"]={
            "ns":_dns.NS,
            "a":_dns.A,
            "txt":_dns.TXT,
            "mx":_dns.MX
        }

    def _IPWhois(self):
        """
        """
        if (not self._response["dns"]
           or not  self._response["dns"].get("a")):
           return
        for ipstr in self._response["dns"]["a"]:
            bw=BasicIPWho(ipstr)
            self._response["ipWho"].update({ipstr:bw.ipWho})

    @property
    def DNS(self):
        """
        """
        return self._response["dns"]

    @property
    def IPWhois(self):
        """
        """
        return self._response["ipWho"]

    @property
    def fullData(self):
        """
        """
        return self._response

    def _run(self):
        """
        """
        self._DNS()
        self._IPWhois()
