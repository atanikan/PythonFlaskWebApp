from flask import Flask

app = Flask(__name__)
app.secret_key = '\\\xfcS\x1e\x8f\xfb]6\x1e.\xa8\xb3\xe1x\xc8\x8e\xc1\xeb5^x\x81\xcc\xd5'
# more secure way is app.config['passkey'] = os.environ.get("KEY")
app.config['passkey'] = "" #set password here


from project import westroutes