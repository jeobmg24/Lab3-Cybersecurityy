import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode, b64encode

d = '''MIIEpAIBAAKCAQEAxUOGZeus3EsRrOoexH+hz2/5OdPv2rJi+uzlQV322KSh+ESH
ayo/4HnpgKSeoLWCaBbJBskIBNhl7g14nIptlP187qEP9jKHjsMvrTB4Oefi69cp
pbHDAP8YKoRY6FdCPTqYcmItkhhslNsGA7BrQWhTZYcpPy116KMZS5dQA+Cr6N7o
Utg4sNoDyTY+IfcDo8v1icivckEI4njU0axyL0ZZpARI62uRiqkS0fR6tet1KFLW
8x1FryZ0qwbV2HXS1zr6SQbgbFgz2d4YPWV8/oVJjTubzmRu3VfD2kWIBYxILkJb
TO4sv/A/SIjBZDsXATOC1LO2n86RU//bbg2BwQIDAQABAoIBAAVWkfUBHzDo8SYC
QenkYE8aQx7O/u8mo6oRrhSKQ+tR7TYoOJfsUUU0V17NVaOYtdo2P6No3kgvSPbb
s3ddAaEmCPL2NdXeQS/aVVh09tPuVAQ40t4yhMnqnU9NPJCxB9BbXRO/V2dcNNgE
Y1HHPOfMuHEHatTUWJv+iekzQ42PQyfn3tmsMc4bQz4enyBA/bAOL+WXy3pHaGwR
sDwSfSYZJctUAqZDBVAyv3g0zzGvttZTZZRG1x0LToNcTtc18y38sTp/a+xQFO7u
v3LTShJj6n4w/IrvN3Dn7Zr4iOato1Ugvz6teKSK+qHyE4ULSpYnWKFugycUDRZr
pF/+FgECgYEAx3YAwDFqTdUxU9UEJi8oPgQD/tPo3W232OO2uF414JqWtkwqKOkd
mjnGzUyhEgsF2oXKp+ubn8z/8kBLGSavKeYNCHKDgkcch9HKvkCbU9svASwMO79/
eyz/jgyBff/JfYs1MVjOtbTyaMOPieQg9XWHL+gQ2J5hVHGlWtSdUeECgYEA/S4V
Hbs5mD93IDNwfQJz13HAm+Aj8S+j3Nq6RcTXwTPuOmf5mJJpKiqx9pHFh6F0k6DW
k/mpJJCbD8fvdOECAKRnuYPaRroy50i3kFLbyTF8HlvrWpWa63GADGQC2UZHTQQv
iXNDABlDrT85PWa5ZkNK660H03SDqO6pfWd/6+ECgYEAnjKGd+j5gk/j9rSNvOdM
CJvQu21BVVYvKbO5+VKncsPJYz7XdWknFGpctfngClp5ww64ZCSnYsAKBA5gQct/
xEB0980zZsGV7FdFcU32pDTEfC5+aWkB6CURb42VquST36Hoh4IDOPUSCmuIzfoE
9gnINgPeUKCVW49jcb4OJKECgYEA9QxNU+GK9Vk4K+qdzeE5ziVDj5t6Lk82AuWR
tUW4rj9dLRrF8m6Da1S3uzeMQKJ8+waJqd/TXpi3/KY/lpjSH10BKAX+lsZRzpoL
UZ1hLXK/94JwYdS7hXbtwRBr0XC8Qkby28674rSRVHYFKPDsMZagRUvMb1YuuKuH
UOGEZwECgYAsQUqUGvhmJxmXKS6rnXOjTEYszxpk5tfxmv9kqo89/ykQyzgr3bgQ
yNQg1wizkA5TD52b00wjAcgpqJUEL9x81ZNPcNaAM4I1SU0nEIXSDCmgS0X4SGWN
P97A0TvZwqDs4JbzBPXTqXo/fyvZqQYhoqtzG1KjqWrSHUQXPDOojQ=='''

p_key = RSA.import_key(b64decode(d))


with open(sys.argv[1], 'rb') as f:
   enc_shared_key = f.read()


   # Decrypt encrypted shared key
   rsa_cipher = PKCS1_v1_5.new(p_key)
   shared_key = b64encode(rsa_cipher.decrypt(enc_shared_key, "Error: failed to decrypt"))


   # Return the value of shared key
   print(str(shared_key)[2:-1])