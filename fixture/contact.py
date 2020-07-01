class ContactHelper:
    def __init__(self, app):
        self.app = app

    def changes_contact_form(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # ввод данных клиента
        self.changes_contact_form("firstname", contact.firstname)
        self.changes_contact_form("lastname", contact.lastname)
        self.changes_contact_form("nickname", contact.nickname)
        # ввод места работы и адрес
        self.changes_contact_form("company", contact.company)
        self.changes_contact_form("address", contact.address)
        # ввод телефонов клиента
        self.changes_contact_form("home", contact.homephone)
        self.changes_contact_form("mobile", contact.mobilephone)
        self.changes_contact_form("work", contact.workphone)
        self.changes_contact_form("fax", contact.fax)
        # ввод электронной почты
        self.changes_contact_form("email", contact.email)
        # дата рождения
        # self.changes_contact_form("bday", contact.bday)
        # # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        # wd.find_element_by_xpath("//option[@value='7']").click()
        # # wd.find_element_by_name("bmonth").click()
        # self.changes_contact_form("bmonth", contact.bmonth)
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        # wd.find_element_by_xpath("//option[@value='July']").click()
        self.changes_contact_form("byear", contact.byear)

    def create_contact(self, contact):
        wd = self.app.wd
        # инициация создание нового контакта
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # подтверждение создания нового контакта
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # переход на экран списка контактов
        self.home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.home_page()

    def modify_first_contact(self, new_info_contact):
        wd = self.app.wd
        # переход на экран списка контактов
        self.home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_info_contact)
        wd.find_element_by_name("update").click()
        self.home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def home_page(self):
        wd = self.app.wd
        if not(len(wd.find_elements_by_name("home")) > 0 and wd.find_element_by_css_selector("div.left:nth-child(7) > input:nth-child(1)")):
            wd.find_element_by_link_text("home").click()

    def count_con(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements_by_name("selected[]"))
