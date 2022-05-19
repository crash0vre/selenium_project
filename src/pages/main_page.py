from src.pages.base_page import BasePage


class MainPage(BasePage):
    #locators
    __signin_link_xp= '//a[@class="login"]'
    __search_box_id= 'search_query_top'
    __search_btn_xp= '//button[@name="submit_search"]'
    __cart_link_xp= '//a[@title="View my shopping cart"]'

    #metods

    def click_signin(self):
        """click sign in link on the top menu"""
        print('Clicking the sign in button')
        self.click_element_by_XP(self.__signin_link_xp)


    def enter_text_in_search(self, phrase): #phrase est fraza
        print(f'Entering "{phrase}" in the search box')
        self.enter_text_by_id(self.__search_box_id, phrase)


    def click_search_btn(self):
        print('Clicking search btn')
        self.click_element_by_XP(self.__search_btn_xp)
