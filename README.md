# connexion-template
A simple template for a connexion app


# To make it run (Linux)

```bash
# Create a python virtual env
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python3 api.py
```

The swagger ui should be available on 127.0.0.1:8080/ui \
And the api available on 127.0.0.1:8080/<endpoint>. For example 127.0.0.1:8080/version
