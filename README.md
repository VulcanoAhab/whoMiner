## About

**whoMiner** Fetch DNS and Hosting data from a domain.


### Installation 


Pip:
```
pip install git+https://github.com/VulcanoAhab/whoMiner
```

### Usage

Import Enrich Module
```
from whoMiner.core import EnrichDomain
```

Fetch Data
```
edn=EnrichDomain("python.org")
edn.fullData

{'domain': 'python.org',
 'dns': {'ns': ['ns-1134.awsdns-13.org.',
   'ns-2046.awsdns-63.co.uk.',
   'ns-484.awsdns-60.com.',
   'ns-981.awsdns-58.net.'],
  'a': ['45.55.99.72'],
  'txt': ['"888acb5757da46ad83b7e341ec544c64"',
   '"_globalsign-domain-verification=MK_ZKmss4D_DdzGOsssHxxBOK6hJc6LGycFvNOESdZ"',
   '"google-site-verification=9852CbTRhQ51-9gCUayPbGYqJeBle_MXLb6E4AL_qQk"',
   '"google-site-verification=QALZObrGl2OVG8lWUE40uVSMCAka316yADn9ZfCU5OA"',
   '"google-site-verification=dqhMiMzpbkSyEhgjGKyEOMlEg2tF0MSHD7UN-MYfD-M"',
   '"google-site-verification=w3b8mU3wU6cZ8uSrj3E_5f1frPejJskDpSp_nMWJ99o"',
   '"status-page-domain-verification=9y2klhzbxsgk"',
   '"v=spf1 mx a:mail.wooz.org ip4:188.166.95.178/32 ip6:2a03:b0c0:2:d0::71:1 include:stspg-customer.com include:_spf.google.com include:mailgun.org ~all"'],
  'mx': ['50 mail.python.org.']},
 'ipWho': {'45.55.99.72': {'asn_query_ip': '45.55.99.72',
   'asn_query_status': 'ok',
   'asn_country': 'US',
   'asn': '14061',
   'asn_name': 'DIGITALOCEAN-ASN - Digital Ocean, Inc.',
   'net_description': 'DigitalOcean, LLC',
   'net_name': 'DIGITALOCEAN-45-55-0-0',
   'net_updated': '2020-04-03'}}}
```


