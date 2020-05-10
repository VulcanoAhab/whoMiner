import os
import re


### baseFiles
_HERE=os.path.abspath(__file__)
_HOME=os.path.expanduser("~")
_HERE=_HERE.replace(_HOME, "")
_ASN_FILE_NAME="asn_name_dict.txt"
_ASN_FILE=os.path.join(_HOME,
    os.path.join(*_HERE.split("/")[:-1], _ASN_FILE_NAME))


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
