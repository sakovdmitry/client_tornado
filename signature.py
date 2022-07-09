import hmac
import hashlib
secret_key = b"n5AUbpMiEGV1WvAcgvjFdm75vDqrvFlm884ZN9IEBjJshGgOouCuNx"
total_params = b"sakovdmitry@gmail.com"
signature = hmac.new(secret_key, total_params, hashlib.sha256).digest()

print(signature)

with open('/Users/dmitrysakov/Dev/filename', 'w') as f:
    f.write('sakovdmitry@gmail.com:')
    f.close()

with open('/Users/dmitrysakov/Dev/filename', 'ba') as f:
    f.write(signature)
    f.close()
