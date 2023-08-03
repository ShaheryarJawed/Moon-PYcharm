import requests
import time

base_url = "https://api.opensea.io/v2/chain/ethereum/contract/0xdd70af84ba86f29bf437756b655110d134b5651c/nfts/{}/refresh"
x_api_key = "66c81eb9fec04c20b247b5d5794e49a6"

def make_api_call(url):
    headers = {"X_API_KEY": x_api_key}
    response = requests.post(url, headers=headers,timeout=1)
    return response.text

def main():
    start_id = 1
    end_id = 10000
    delay_seconds = 1

    for i in range(start_id, end_id + 1):
        url = base_url.format(i)
        try:
            response_text = make_api_call(url)
            print(f"API Call {i}: Response Text - {response_text}")
        except requests.exceptions.RequestException as e:
            print(f"API Call {i}: Error occurred - {e}")

        time.sleep(delay_seconds)

if __name__ == "__main__":
    main()
