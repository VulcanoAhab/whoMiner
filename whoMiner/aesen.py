import re


### baseFiles
_ASN_FILE="asn_name_dict.txt"

### data producers
def build_asn_dict():
    '''
    '''
    rex_asn=re.compile(r"(AS[\d]+)[\s\t]+(.*)")
    fd=open(_ASN_FILE, "r")
    number_name_list=rex_asn.findall(fd.read())
    fd.close()
    asn_dict=dict(number_name_list)
    return asn_dict
