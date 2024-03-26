#Nessesary imports
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os

#Get request
def get_page_data(url):
    return requests.get(url).text


#Print results
def show_results(data):
    print(tabulate(data, headers="firstrow"))

#Clear screan
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux and Mac
    else:
        _ = os.system('clear')


#Main function
def main():
    clear_screen()
    #Some variable that will help to get a nice output
    pos = ["Rank"]
    rank = 1
    name = ["Name"]
    price = ["Price"]
    
    #To get html forom web page
    url = "https://crypto.com/price"
    page = get_page_data(url)

    #Create a bs4 object to use the, required funtions
    soup = BeautifulSoup(page,"html.parser")
    coins = soup.find_all("tr",class_="css-1cxc880")

    #Using a loop to to cycle throught blocks of html, to get wanted information
    for coin in coins:
        pos.append(rank)
        rank += 1

        name_coin = coin.find("p", class_="chakra-text css-rkws3").text
        name.append(name_coin)

        price_coin = coin.find("div", class_="css-b1ilzc").text
        price.append(price_coin)
        
    #Printing all the information in a nice,formatted and neat way
    data = list(zip(pos,name,price))
    show_results(data)


if __name__ == "__main__":
    main()