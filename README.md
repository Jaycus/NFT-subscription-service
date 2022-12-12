# NFT-subscription-service

A Python script for signing up for and getting the monthly NFT collection from an NFT subscription service.

##Requirements
Python 3.6 or later
requests module
Usage
To use the script, run the following command:
python nft_subscription.py

The script will prompt you to enter your email address and desired membership level (1-3), and then sign you up for the NFT subscription. It will then retrieve the current month's NFT collection and print it to the console.

##Functions
The script defines the following functions:

sign_up_for_nft_subscription()
This function prompts the user for their email address and membership level, and sends a POST request to the NFT subscription service to sign up.

get_monthly_nft_collection()
This function sends a GET request to the NFT subscription service to get the current month's NFT collection, and prints the collection to the console.
