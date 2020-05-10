from whoMiner.aesen import build_asn_dict
from ipwhois import IPWhois

import json
import re


class BasicIPWho:
    """
    """
    _ASN_DICT=build_asn_dict()
    _XDATIS=re.compile(r"\d{4}-\d{2}-\d{2}")

    @classmethod
    def upis_date(cls, whois_dict):
        """
        """
        if not "updated" in whois_dict:return 0
        dis=cls._XDATIS.findall(whois_dict["updated"])
        if not dis:return 0
        return int(dis[0].replace("-",""))

    def __init__(self, ipstr):
        """
        """
        self._ip=ipstr
        self._response={"asn_query_ip":self._ip}
        self._rawResponse={}

    @property
    def ipWho(self, renew=False):
        """
        fetch only basic asn and latest network data
        """
        if "asn_query_status" in self._response and not renew:
            return self._response

        try:
            obj=IPWhois(self._ip)
            self._rawResponse = obj.lookup_whois(inc_nir=True)
            self._response["asn_query_status"]="ok"
        except:
            self._response["asn_query_status"]="fail"
        self._response["asn_country"]=self._rawResponse["asn_country_code"]
        self._response["asn"]=self._rawResponse["asn"]
        if self._rawResponse["asn"]:
            key="".join(["AS",self._rawResponse["asn"]])
            self._response["asn_name"]=self._ASN_DICT.get(key, "UNKOWN")
        if self._rawResponse["nets"]:
            ####get most recent net data
            net=sorted(self._rawResponse["nets"],
                        key=BasicIPWho.upis_date,
                        reverse=True)[0]
            self._response["net_description"]=net["description"]
            self._response["net_name"]=net["name"]
            self._response["net_updated"]=net["updated"]

        return self._response
