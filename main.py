import requests

# Function to sign up for NFT subscription
def sign_up_for_nft_subscription():
  # Prompt user for email address
  email = input("Enter your email address: ")
  # Prompt user for membership level
  level = int(input("Please enter your desired membership level (1-3): "))

  # Send a POST request to the NFT subscription service to sign up
  response = requests.post("https://nft-subscription-service.com/signup", json={"email": email, "level": level})

  # Handle response
  if response.status_code == 200:
    print("Successfully signed up for NFT subscription!")
  else:
    print("Failed to sign up for NFT subscription. Please try again.")

# Function to get monthly NFT collection
def get_monthly_nft_collection():
  # Send a GET request to the NFT subscription service to get the current month's collection
  response = requests.get("https://nft-subscription-service.com/collection")

  # Handle response
  if response.status_code == 200:
    # Print the NFTs in the collection
    print("Here is this month's NFT collection:")
    for nft in response.json()["nfts"]:
      print(nft)
  else:
    print("Failed to get monthly NFT collection. Please try again.")

# Sign up for the NFT subscription
sign_up_for_nft_subscription()

# Get the current month's NFT collection
get_monthly_nft_collection()
