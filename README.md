# phoenix_python_client

## Requirement:
```

git clone https://github.com/apache/phoenix-queryserver.git

git clone https://github.com/samircaica/phoenix_python_client.git

cd phoenix_python_client

./test_phoenixdb.sh <Local python dir> <principal> <keytab> <krb5.conf> <PQS host> <PQS port> test.py

example:

./test_phoenixdb.sh ~/phoenix-queryserver  principal-abc@DOMAIN.ORG ~/principal.keytab ~/krb5.conf http://my_PQS_FQDN 8765 test.py

```
