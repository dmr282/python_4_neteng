from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

nonaes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")

for i in nonaes:
    print i.text
    for i in nonaes:
        print i.children
