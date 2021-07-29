import requests

def free_api():
    url = "https://gorest.co.in/public/v1/users"
    response = requests.get(url)
    return(response)

if __name__ == "__main__":
    free_api()