from selenium.webdriver.common.by import By




class WebElements(object):
    # path to the chrome driver
    path_google_chrome = "../../chromedriver.exe"
    # URL of the main page
    url_main = "https://www.amazon.com/"

    # ID of web elements
    ########################################
    # ID of the search field
    search_field = (By.ID, 'twotabsearchtextbox')
    # ID of chosen country where to deliver
    deliver_country = (By.ID, 'glow-ingress-line2')
    # ID of the cart
    cart = (By.ID, "nav-cart")
    # ID of a banner list
    banner_list = (By.ID, 'desktop-banner')
    # ID of the button to add item to the cart
    id_add_to_cart = 'add-to-cart-button'
    # ID of the button to proceed to checkout after a item added to cart
    id_cart_proceed_to_checkout = 'hlb-ptc-btn-native'

    ########################################
    # xpath to the first item in the search
    xpath_first_search_output = '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'