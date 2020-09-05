import hashlib
import hmac
import base64

password = "malik"
hashedWord = hashlib.sha256(password.encode()).hexdigest()
print(hashedWord)


password = "junaid"
hashedWord = hashlib.sha256(password.encode()).hexdigest()
print(hashedWord)


password = "fiaz"
hashedWord = hashlib.sha256(password.encode()).hexdigest()
print(hashedWord)


password = "malikjunaidfiaz"
hashedWord = hashlib.sha256(password.encode()).hexdigest()
print(hashedWord)

dig = hmac.new(b'malik', msg=password.encode(), digestmod=hashlib.sha256).digest()
print(dig)
print(base64.b64encode(dig).decode())