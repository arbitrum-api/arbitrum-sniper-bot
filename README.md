# SushiSwap Token Purchase Bot

This Python bot allows you to automatically purchase tokens from the **SushiSwap** decentralized exchange (DEX) on the **Arbitrum** network using the **Ethereum (ETH)** cryptocurrency. The bot connects to the **Arbitrum** network, checks the gas price, and submits transactions to purchase a specified token via the SushiSwap router contract.

## Features
- Connects to the **Arbitrum** blockchain via RPC.
- Fetches the **current gas price** from the Arbitrum API.
- Allows the user to **buy tokens** from **SushiSwap** by swapping **ETH** for a specified token.
- **Supports automatic gas adjustment** to ensure the transaction is processed efficiently.
- Uses your **private key** to sign the transaction securely.

## Prerequisites
Before using the bot, you need to install the following dependencies:
- **Python 3.x**
- **requests** (for making HTTP requests)
- **web3.py** (for interacting with the Ethereum blockchain)
- **eth_account** (for Ethereum account management)

To install the required dependencies, run the following command:

```bash
pip install requests web3 eth_account

How it works

    Get the current gas price from the Arbitrum API.
    Check your token balance (optional) by querying the balanceOf function of the token contract.
    Generate and send the transaction:
        The bot prepares a transaction that swaps ETH for the token you want to buy using the SushiSwap Router Contract.
        The transaction is sent with the specified gas price and gas limit to the Arbitrum network via the Arbitrum API.
    Once the transaction is confirmed, the bot will print the transaction hash if successful.

Example Flow

    The bot will attempt to buy 1 token (adjustable in the code) by swapping 0.1 ETH for the token specified in the TOKEN_ADDRESS.
    The bot will automatically set a 10-minute deadline for the transaction and use the current gas price to set the gas fee for the transaction.

Security Considerations

    Private key management: Do not hard-code your private key in production code. Use environment variables or secure vault services to store sensitive information securely.
    Ensure that you are interacting with the correct contract address and that the token is available on the SushiSwap exchange.

Troubleshooting

    If the transaction fails, check the error message returned by the Arbitrum API for more details.
    Ensure that your wallet has enough ETH to cover both the token purchase and the gas fees.

Disclaimer

This bot is for educational purposes only. Use it at your own risk. Always double-check your contract addresses and ensure you’re interacting with trusted decentralized exchanges.
