import uuid
from Crypto.PublicKey import RSA

def generate_user_credentials():
    user_uuid = uuid.uuid4().hex
    key = RSA.generate(2048)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return user_uuid, public_key, private_key
