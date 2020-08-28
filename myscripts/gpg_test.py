#!/usr/bin/env python3
import yaml
import sys

file_name = 'source-build.yaml'
stream = open(file_name, 'r')
data = yaml.load(stream, Loader=yaml.FullLoader)

class PSS(str):
    pass


if data.get('repositories'):
    #key_str = '-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQENBFRj9wABCADBxfCOCydUqsXS4JlhytBZroc7129AGHTn62xanKYXN1ihB5Ay\npLGJcz22MHnCegcCUA6HXOaOdLJTg8PZp/ncOGcLjRsmy+tkQzC0aX0yKhH1bKxe\nTKe2/Kdk7y8SwW3Uw2r+R/d36DUoCTCRmibScIM4clD4eOOz/FZEVbnZuGmEKw1z\nO5oMDgerEm8ou4s45RwIfTyt2UodxhLpjBWvuMKhKvc8JlpiZD/TMj+/uMhDe/eL\nijG+tMi9vUdo1B4xsDlLW7GFCmYXMBzhuO30TaC9PSE2e2cQS1jWX4113l32oXdg\nIP8Nl1yxFGDPAKLQe+HNt7gyhoEkPP6tUKARABEBAAG0H1JPUyBSZWxlYXNlIDxu\nb29uZUBleGFtcGxlLmNvbT6JATgEEwECACIFAlRj9wACGwMGCwkIBwMCBhUIAgkK\nCwQWAgMBAh4BAheAAAoJEIsjFZ/llEM2cx8H/Ru8upiYAhwphPxOPEvkLfqZDEjI\nLrFg4A5WhUvhMFpRzdOUovVCM9D73rtZEsaQgmtPIs1Mdp8M44E5G7sV9Zjp/4zf\nT/vgopfBjG9M3foWkhWyupFlHm7AC9tv+3+vmzW5uzvrk/tRqirpU/5lm+wEE+Xq\nJy2UlkGj8o1WZDJXd0SoJF/MRXBwOa9kkpxNMLrOGSSra9GzBsIO9570QAUOD8pA\nOKD+5pjDIdnySDpfBNIhv029dBhSKZg5sTzZr3dxise759l0W+8i1H6GUvxWe4km\n8v7YDPyajsHs43ImbZQrMcr5l1TAVk8OBSLqGmtiLasRFnHQUxQyJNyo3gS5AQ0E\nVGP3AAEIAM+qLZEg9qagVbm/FvS1wGlQVFgokjWGIZCxbzC2mNNAmyNXvOeCD899\nN0xnprYd131Ocg53tllkYeSyUNBfO0f/CI0Msh+hzDivT0HqJxmxZGWHrm35to4e\nLSIAOmoxDNXQwpC4ZNTUPZNNFdCfU0tGGXnA66BYpilfEv20eBgk1x+pu1vJxne1\n/SPUwZAiiWb2ydRHvLJErUTcXGKn5UG4PlUAOCCoBC3195TIevlO9hlvtLkW9olu\nhnWNtJJHfbjtwoQC+z5Kn4miFl/FkXAp8YfYSCF3glXAXY08dLIJkFCyi07J3jj6\nI6xX0An+i8P/k/DyldjaMoutARLswuMAEQEAAYkBHwQYAQIACQUCVGP3AAIbDAAK\nCRCLIxWf5ZRDNpN5CACdKoLcjJIIPQuCPyLdba5z6prRRo21Yud5dtyGGhOmDAt/\ncjlmdwlta/ZkArkTB9is4iIDvo2D4PmRA756VHEBfhqwknt5DANMm3p9A5/z+sgX\nn/punYuskxDjOU2+NwbBXRHgXz1vQpIEVtS3bQvjmyPn/yl31NM5zZ9Lwat/ynKj\niAvRflohugScLVSA0VCvn4gKlxCHBvtNS22rvsPW2zbOz38pp5gU+fNRUaLRmHna\nb97l/64k31UzIQHeAHHbGODQfJ0PpKyS9UM4vvcMldUrBL4O4fLVaeqMjAhKSfcY\nxaePFwP+okKW1h9qvwFhNF0JSCtdJrexdCf8jGE7\n=E8ot\n-----END PGP PUBLIC KEY BLOCK-----\n'
    key_str = PSS("""\
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1
mQENBFRj9wABCADBxfCOCydUqsXS4JlhytBZroc7129AGHTn62xanKYXN1ihB5Ay
pLGJcz22MHnCegcCUA6HXOaOdLJTg8PZp/ncOGcLjRsmy+tkQzC0aX0yKhH1bKxe
TKe2/Kdk7y8SwW3Uw2r+R/d36DUoCTCRmibScIM4clD4eOOz/FZEVbnZuGmEKw1z
O5oMDgerEm8ou4s45RwIfTyt2UodxhLpjBWvuMKhKvc8JlpiZD/TMj+/uMhDe/eL
ijG+tMi9vUdo1B4xsDlLW7GFCmYXMBzhuO30TaC9PSE2e2cQS1jWX4113l32oXdg
IP8Nl1yxFGDPAKLQe+HNt7gyhoEkPP6tUKARABEBAAG0H1JPUyBSZWxlYXNlIDxu
b29uZUBleGFtcGxlLmNvbT6JATgEEwECACIFAlRj9wACGwMGCwkIBwMCBhUIAgkK
CwQWAgMBAh4BAheAAAoJEIsjFZ/llEM2cx8H/Ru8upiYAhwphPxOPEvkLfqZDEjI
LrFg4A5WhUvhMFpRzdOUovVCM9D73rtZEsaQgmtPIs1Mdp8M44E5G7sV9Zjp/4zf
T/vgopfBjG9M3foWkhWyupFlHm7AC9tv+3+vmzW5uzvrk/tRqirpU/5lm+wEE+Xq
Jy2UlkGj8o1WZDJXd0SoJF/MRXBwOa9kkpxNMLrOGSSra9GzBsIO9570QAUOD8pA
OKD+5pjDIdnySDpfBNIhv029dBhSKZg5sTzZr3dxise759l0W+8i1H6GUvxWe4km
8v7YDPyajsHs43ImbZQrMcr5l1TAVk8OBSLqGmtiLasRFnHQUxQyJNyo3gS5AQ0E
VGP3AAEIAM+qLZEg9qagVbm/FvS1wGlQVFgokjWGIZCxbzC2mNNAmyNXvOeCD899
N0xnprYd131Ocg53tllkYeSyUNBfO0f/CI0Msh+hzDivT0HqJxmxZGWHrm35to4e
LSIAOmoxDNXQwpC4ZNTUPZNNFdCfU0tGGXnA66BYpilfEv20eBgk1x+pu1vJxne1
/SPUwZAiiWb2ydRHvLJErUTcXGKn5UG4PlUAOCCoBC3195TIevlO9hlvtLkW9olu
hnWNtJJHfbjtwoQC+z5Kn4miFl/FkXAp8YfYSCF3glXAXY08dLIJkFCyi07J3jj6
I6xX0An+i8P/k/DyldjaMoutARLswuMAEQEAAYkBHwQYAQIACQUCVGP3AAIbDAAK
CRCLIxWf5ZRDNpN5CACdKoLcjJIIPQuCPyLdba5z6prRRo21Yud5dtyGGhOmDAt/
cjlmdwlta/ZkArkTB9is4iIDvo2D4PmRA756VHEBfhqwknt5DANMm3p9A5/z+sgX
n/punYuskxDjOU2+NwbBXRHgXz1vQpIEVtS3bQvjmyPn/yl31NM5zZ9Lwat/ynKj
iAvRflohugScLVSA0VCvn4gKlxCHBvtNS22rvsPW2zbOz38pp5gU+fNRUaLRmHna
b97l/64k31UzIQHeAHHbGODQfJ0PpKyS9UM4vvcMldUrBL4O4fLVaeqMjAhKSfcY
xaePFwP+okKW1h9qvwFhNF0JSCtdJrexdCf8jGE7
=E8ot
-----END PGP PUBLIC KEY BLOCK-----
""")
    def pss_representer(dumper, data):
        style = '|'
        tag = u'tag:yaml.org,2002:str'
        return dumper.represent_scalar(tag, data, style=style)
    yaml.add_representer(PSS, pss_representer, Dumper=yaml.SafeDumper)
    #key_str = key_str.strip()
    data['repositories']['keys'] = [key_str]
    with open(file_name, 'w') as f:
        yaml.safe_dump(data,f)
