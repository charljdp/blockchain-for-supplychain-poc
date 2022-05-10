from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'http://localhost:9984'

bdb = BigchainDB(bdb_root_url)

bicycle = {
    'data': {
        'bicycle': {
            'serial_number': 'abcd1234',
            'manufacturer': 'bkfab',
        },
    },
}

alice, bob = generate_keypair(), generate_keypair()

print(
    'pub:', alice.public_key, '\n',
    'pri', alice.private_key
)