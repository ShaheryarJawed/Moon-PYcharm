import requests
import time

def refresh_nft(url, api_key):
    """This method refresh_nft is for sending post API requests and handling all the exceptions
        @:param url: is the url of the api to which we are sending requests
        @:param api_key: we are passing api key to function for sending post request (post requests requires api key) """

    headers = {"X_API_KEY": api_key}
    try:
        r = requests.post(url, headers=headers, timeout=30)
        return r.text
    except requests.exceptions.Timeout:
        print(f"API CALL: Timeout occurred for {url}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"API CALL: An error occurred for {url} - {e}")
        return None


def main():
    """This main method is  for iterating the number of requests and for for changing the nft tokken id each time it iterate and put delay in each request """

    base_url = "https://api.opensea.io/v2/chain/ethereum/contract/0xdd70af84ba86f29bf437756b655110d134b5651c/nfts/"
    api_key = "66c81eb9fec04c20b247b5d5794e49a6"
    iterations = 10000
    time_delay = 1  # Time delay between each request in seconds

    try:
        for i in range(1, iterations + 1):
            url = f"{base_url}{i}/refresh"

            response = refresh_nft(url, api_key)
            if response is not None:
                print(f"API CALL {i}: {response}")

            time.sleep(time_delay)
    except KeyboardInterrupt:
        print("User terminated the script.")


if __name__ == "__main__":
    main()