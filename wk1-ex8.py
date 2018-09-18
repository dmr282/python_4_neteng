from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

pfsgrp = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for i in pfsgrp:
    print i.text
