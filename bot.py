import requests
from web3 import Web3
from eth_account import Account

# Connect to Arbitrum RPC
web3 = Web3(Web3.HTTPProvider('https://arbitrum-api.co/api'))

# SushiSwap Router address on Arbitrum
SUSHISWAP_ROUTER_ADDRESS = '0x1b02a8cb5d3e4c8f9fb8f3b58cd5cb5d0f6e2b3f'
TOKEN_ADDRESS = '0xTokenAddressHere'  # Replace with the actual token address
private_key = '0xYourPrivateKeyHere'  # Replace with your private key
SENDER_ADDRESS = '0xYourAddressHere'  # Replace with your address

# Function to get current gas price from Arbitrum API
def get_gas_price():
    response = requests.get('https://arbitrum-api.co/api/v1/gas-price')
    data = response.json()
    return int(data['gasPrice'])

# Function to get token balance for a given address
def get_balance(address, token_address):
    token_contract = web3.eth.contract(address=token_address, abi=[{
        "constant": True,
        "inputs": [{"name": "account", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }])
    balance = token_contract.functions.balanceOf(address).call()
    return balance

# Function to send the transaction via Arbitrum API
def send_transaction(private_key, tx_data):
    url = 'https://arbitrum-api.co/api/v1/transaction'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'private_key': private_key,
        'transactionData': tx_data
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    if data['status'] == 'success':
        print("Transaction successful:", data['txHash'])
    else:
        print("Transaction error:", data['error'])

# Function to initiate token purchase via SushiSwap
def buy_token_via_sushiswap():
    gas_price = get_gas_price()
    token_amount = 1  # Example: buying 1 token

    # Prepare the transaction data for swapping ETH for tokens via SushiSwap
    tx_data = {
        'from': SENDER_ADDRESS,
        'to': SUSHISWAP_ROUTER_ADDRESS,
        'data': web3.eth.contract(
            address=SUSHISWAP_ROUTER_ADDRESS, 
            abi=[{
                "name": "swapExactETHForTokens",
                "type": "function",
                "inputs": [
                    {"name": "amountOutMin", "type": "uint256"},
                    {"name": "path", "type": "address[]"},
                    {"name": "to", "type": "address"},
                    {"name": "deadline", "type": "uint256"}
                ]
            }]
        ).encodeABI(
            fn_name='swapExactETHForTokens',
            args=[
                web3.toWei('0.1', 'ether'),
                [web3.toChecksumAddress('0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE'), web3.toChecksumAddress(TOKEN_ADDRESS)],
                SENDER_ADDRESS,
                int(web3.eth.get_block('latest')['timestamp']) + 60 * 10
            ]
        ),
        'value': web3.toWei('0.1', 'ether'),
        'gas': 200000,
        'gasPrice': web3.toWei(str(gas_price), 'gwei'),
        'nonce': web3.eth.getTransactionCount(SENDER_ADDRESS),
    }

    send_transaction(private_key, tx_data)
    print('Token purchase transaction has been initiated!')

# Run the function to buy tokens via SushiSwap
buy_token_via_sushiswap()
