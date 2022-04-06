# blockchain-for-supplychain-poc
A proof of concept of blockchain used for a supply chain tracking application. This POC will just be an API. Each use case
can be represented by an API call.

## Use cases
- Register an authorized node
    - Generate public/private key pair
- Deregister a node
- Add transaction(s)
    - Add asset(s)
    - Remove asset(s)
    - Update asset(s) status
- Query transaction(s)
    - Find asset(s)
    - Audit asset(s)

# Dependencies
[BigChainDB driver](https://github.com/bigchaindb/bigchaindb-driver)  
[Flask](https://flask.palletsprojects.com/en/2.1.x/)