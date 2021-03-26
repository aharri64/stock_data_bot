class StockData:
    def __init__(self):
        '''Initialize an instance of StockData'''
        self.raw_data = []
        self.data = []
        self.urls = {
            'sign_in': 'https://wallmine.com/users/sign-in',
            'homepage': 'https://wallmine.com/',
            'view_stock': lambda exchange, symbol: f'https://wallmine.com/{exchange}/{symbol}'
        }
        # use your path to your Chromedriver
        self.driver = webdriver.Chrome(
            '/Users/romebell/downloads/chromedriver-4')

    def login(self):
        '''Method used to login into Wallmine account'''
        self.driver.get(urls['sign_in'])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/div[1]/div[2]/a').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
        time.sleep(.2)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/div[2]/div[1]/button').click()
        time.sleep(3)
        if self.driver.find_element_by_xpath('/html/body/main/section/div[2]/div/div[1]/h1/span'):print('Login Was Successful')

    def retrieve_data(self):
        '''Method use to retrieve stock data from Wallmine'''

    def parse_data(self):
        '''Method used to parse the data that was retrieved'''

    def store_data(self):
        '''Method used to store the data inside a MongoDB database'''

    def view_stock(self, ticker):
        '''Method used to view a stock'''
        # View the webpage and return a string of the stock info

    def compare_price(self, exchange, symbol):
        '''Method used to compare the current price of a stock to the price in the database'''
        # Return an object with the realtime price and price in database

    def stop_program(self):
        '''Method used to close the program'''
        print('Closing program in 5 seconds...')
        time.sleep(5)
        self.driver.close()
