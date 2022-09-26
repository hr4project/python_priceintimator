from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from bs4 import BeautifulSoup
import sys
import requests
import smtplib
import webbrowser
import validators

class PageWindow(QMainWindow):
    gotoSignal = pyqtSignal(str)

    def goto(self, name):
        self.gotoSignal.emit(name)

class MainWindow(PageWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : #aee6e6;")

        self.setWindowTitle("Price Intimator")

        button = QPushButton("",self)
        button.setGeometry(100, 100, 0, 0)
        button.resize(100, 100)
        button.setStyleSheet("background-image : url(amazon1.png);")
        button.clicked.connect(self.make_handleButton("amazonbutton"))


        button1 = QPushButton("",self)
        button1.setGeometry(300,100,0,0)
        button1.resize(100,100)
        button1.setStyleSheet("background-image : url(american1.png);")
        button1.clicked.connect(self.make_handleButton("americanbutton"))

        button2 =QPushButton("", self)
        button2.setGeometry(500, 100, 0, 0)
        button2.resize(100, 100)
        button2.setStyleSheet("background-image : url(dell1.png);")
        button2.clicked.connect(self.make_handleButton("dellbutton"))

        button3 = QPushButton("", self)
        button3.setGeometry(700, 100, 0, 0)
        button3.resize(100, 100)
        button3.setStyleSheet("background-image : url(ebay1.png);")
        button3.clicked.connect(self.make_handleButton("ebaybutton"))

        button4 = QPushButton("", self)
        button4.setGeometry(900, 100, 0, 0)
        button4.resize(100, 100)
        button4.setStyleSheet("background-image : url(flipkart1.png);")
        button4.clicked.connect(self.make_handleButton("flipkartbutton"))

        button5 = QPushButton("", self)
        button5.setGeometry(100, 300, 0, 0)
        button5.resize(100, 100)
        button5.setStyleSheet("background-image : url(hp1.png);")
        button5.clicked.connect(self.make_handleButton("hpbutton"))

        button6 = QPushButton("", self)
        button6.setGeometry(300, 300, 0, 0)
        button6.resize(100, 100)
        button6.setStyleSheet("background-image : url(shop1.png);")
        button6.clicked.connect(self.make_handleButton("shopbutton"))
        button7 = QPushButton("", self)
        button7.setGeometry(500, 300, 0, 0)
        button7.resize(100, 100)
        button7.setStyleSheet("background-image : url(shopclues1.png);")
        button7.clicked.connect(self.make_handleButton("shopcluesbutton"))

        button8 = QPushButton("", self)
        button8.setGeometry(700, 300, 0, 0)
        button8.resize(100, 100)
        button8.setStyleSheet("background-image : url(snapdeal1.png);")
        button8.clicked.connect(self.make_handleButton("snapdealbutton"))

        button9 = QPushButton("", self)
        button9.setGeometry(900, 300, 0, 0)
        button9.resize(100, 100)
        button9.setStyleSheet("background-image : url(walmart2.png);")
        button9.clicked.connect(self.make_handleButton("walmartbutton"))

    def make_handleButton(self,button):
        def handlebutton():
            if button=="amazonbutton":
                self.goto("amazon")
            elif button=="americanbutton":
                self.goto("american")
            elif button=="dellbutton":
                self.goto("dell")
            elif button=="ebaybutton":
                self.goto("ebay")
            elif button=="flipkartbutton":
                self.goto("flipkart")
            elif button=="hpbutton":
                self.goto("hp")
            elif button=="shopbutton":
                self.goto("shop")
            elif button=="shopcluesbutton":
                self.goto("shopclues")
            elif button=="snapdealbutton":
                self.goto("snapdeal")
            elif button=="walmartbutton":
                self.goto("walmart")
        return handlebutton

class amazon(PageWindow):
      def __init__(self):
        super().__init__()
        self.setWindowTitle("AMAZON")
        self.setGeometry(0, 0, 1000, 1000)
        self.setStyleSheet("background-color : #e4f9ff;")
        button = QPushButton("", self)
        button.resize(30,30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))
        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))
        self.url =QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("",self)
        self.error.move(100, 600)
        self.error.resize(150,30)
        self.error.setFont(QFont('Arial',15))
        self.error_user = QLabel("",self)
        self.error_user.move(250,600)
        self.error_user.resize(500,30)
        self.error_user.setFont(QFont('Arial',15))

      def search(self):
        webbrowser.open("https://www.amazon.in/?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_Cj0KCQiAk53-BRD0ARIsAJuNhpsTbyhtCce720aJaLshItAzEilX3EKSTjTQRxNNc_25GXTta2PMlOEaAhgJEALw_wcB_k_&ext_vrnc=hi&gclid=Cj0KCQiAk53-BRD0ARIsAJuNhpsTbyhtCce720aJaLshItAzEilX3EKSTjTQRxNNc_25GXTta2PMlOEaAhgJEALw_wcB")

      def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("amazon")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("amazon")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

      def ok(self):
          headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
          url = self.url.text()
          URL1 = str(url)
          price = self.price.text()
          PRICE = str(price)
          page = requests.get(URL1, headers=headers)
          soup = BeautifulSoup(page.content, 'html.parser')
          title = str(soup.find(lang="en-in"))
          title = title.replace('class', 'id')
          soup1 = BeautifulSoup(title, 'html.parser')

          if soup1.find(id="productTitle"):
              title1 = soup1.find(id="productTitle").get_text(strip=True)
              self.Title.setText(title1)

          if soup1.find(id="priceblock_dealprice"):
              price = soup1.find(id="priceblock_dealprice").get_text(strip=True)
              price1 = price[2:]
              price2 = price1.replace(',', '')
              price3 = float(price2)
              self.product_price.setText(price)
          elif soup1.find(id="priceblock_ourprice"):
              price = str(soup1.find(id="priceblock_ourprice").get_text(strip=True))
              price1 = price.replace('-', '')
              price2 = price1.replace('₹', '')
              price3 = price2.strip()
              price4 = price3.replace('  ', ',')
              index = price4.index(',')
              price5 = price4[0:index]
              price6 = price4[index + 1:].strip()
              self.product_price.setText(price)

          elif soup1.find(id="priceblock_sellprice"):
              price = soup1.find(id="priceblock_sellprice").get_text(strip=True)
              price1 = price[2:]
              price2 = price1.replace(',', '')
              price3 = float(price2)
              self.product_price.setText(price)

          elif soup1.find(id="a-color-base"):
              price = soup1.find(id="a-color-base").get_text(strip=True)
              self.product_price.setText(price)
              price1 = price[2:]
              price2 = price1.replace(',', '')
              price3 = float(price2)

          else:
              self.errors()

          if self.price.text():
              if price3 <= PRICE:
                  self.sendmail()
              elif price5 <= PRICE >= price6:
                  self.sendmail()
              else:
                  self.error.setText("ERROR :")
                  self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
          else:
              self.error.setText("ERROR :")
              self.error_user.setText("PLEASE INSERT THE PRICE")

          def errors(self):
              self.error.setText("ERROR :")
              self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

      def sendmail(self):
          url = self.url.text()
          URL1 = str(url)
          mail = self.mail.text()
          MAIL_USER = str(mail)
          if self.mail.text():
              server = smtplib.SMTP('smtp.gmail.com', 587)
              server.ehlo()
              server.starttls()
              server.ehlo()
              server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')
              subject = 'PRICE FELL DOWN '
              body = 'check out the following amazon link', URL1
              msg = f"Subject:{subject}\n\n{body}"
              server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)
              print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

              server.quit()
          else:
              self.error.setText("ERROR :")
              self.error_user.setText("Invalid Mail id try again")

      def goToMain(self):
              self.goto("main")

# -------------------------------------------------#---------------------------------------------------

class american(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("AMERICAN TOURISTER")
        self.setGeometry(0, 0, 1000, 1000)
        self.setStyleSheet("background-color : #e3f6f5")
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))
        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))
        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)

        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))

    def search(self):
        webbrowser.open(
            "https://shop.americantourister.com/")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("american")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("american")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")


    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        price = self.price.text()
        PRICE = str(price)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(id="main"))
        title1 = title.replace('class', 'id')
        soup1 = BeautifulSoup(title1, 'html.parser')
        if soup1.find(id="product-name"):
            title2 = soup1.find(id="product-name").get_text(strip=True)
            price = soup1.find(id="price-current").get_text(strip=True)
            price1 = price.strip()
            price2 = price1[1:]
            price3 = float(price2)
            self.Title.setText(title2)
            self.product_price.setText(price)
        else:
            self.errors()
            if self.price.text():
                if price3 <= PRICE:
                    self.sendmail()
                else:
                    self.error.setText("ERROR :")
                    self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("PLEASE INSERT THE PRICE")

    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')

            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")
    def goToMain(self):
        self.goto("main")


# --------------------------------------------------------------------------------------------------------------------------------------
class dell(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("DELL")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))

        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))
    def search(self):
        webbrowser.open(
            "https://www.dell.com/en-in/work/shop/deals?~ck=mn&gacd=9683528-9006-5761040-271724588-0&dgc=ST&&gclid=CjwKCAiAn7L-BRBbEiwAl9UtkFq489qWKgclXNah3ANewWQpoIFr7yHIhIxj7fAqNsCleAY_cOiORBoCd7cQAvD_BwE&gclsrc=aw.ds")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("dell")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("dell")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")
    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(lang="en"))
        title1 = title.replace('class', 'id')
        soup1 = BeautifulSoup(title1, 'html.parser')
        if soup1.find(id="cf-pg-title"):
            title2 = soup1.find(id="cf-pg-title").get_text(strip=True)
            price = soup1.find(id="cf-price js-tooltip-trigger").get_text(strip=True)
            price1 = price.strip()
            price2 = price1[2:]
            price3 = price2.replace(',', '')
            price4 = float(price3)
            self.Title.setText(title2)
            self.product_price.setText(price)
        else:
            self.errors()
        price = self.price.text()
        PRICE = str(price)
        if self.price.text():
            if price4 <= PRICE:
                self.sendmail()
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")

    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')

            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")

    def goToMain(self):
        self.goto("main")


class ebay(PageWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("eBAY")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))
        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)


        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))
    def search(self):
        webbrowser.open(
            "https://www.ebay.com/")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("ebay")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("ebay")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")

    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if soup.find(id='itemTitle'):
            title = soup.find(id='itemTitle').get_text(strip=True)
            title1 = title[16:]
            price = soup.find(id="prcIsum").get_text(strip=True)
            self.Title.setText(title)
            self.product_price.setText(price)


        elif soup.find(id='prp-container-wrapper'):
            title = str(soup.find(id='prp-container-wrapper'))
            title1 = title.replace('class', 'id')
            soup1 = BeautifulSoup(title1, 'html.parser')
            title2 = soup1.find(id="product-title").get_text(strip=True)
            price = soup1.find(id="display-price").get_text(strip=True)
            self.Title.setText(title2)
            self.product_price.setText(price)

        else:
            self.errors()
        PRICE = str(self.price.text())
        if self.price.text():
            if price <= PRICE:
                self.sendmail()

            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")

    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')

            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")


    def goToMain(self):
        self.goto("main")

#----------------------------------------------------------------------------
class flipkart(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("FLIPKART")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))
        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))

        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))

        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))

    def search(self):
        webbrowser.open(
            "https://www.flipkart.com/?gclid=CjwKCAiAn7L-BRBbEiwAl9UtkDE5Of6orCG1z5cq3b7I83Ly462gNSXrb6zkKkClt9rtH9jyVSWqxRoCyiUQAvD_BwE&ef_id=CjwKCAiAn7L-BRBbEiwAl9UtkDE5Of6orCG1z5cq3b7I83Ly462gNSXrb6zkKkClt9rtH9jyVSWqxRoCyiUQAvD_BwE:G:s&s_kwcid=AL!739!3!326505318642!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_city_goog")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)
                if self.buttonReply == QMessageBox.Yes:
                    self.goto("flipkart")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("flipkart")
                    self.my_web.close()
                else:
                    self.errors()

            else:
                self.error.setText("ERROR :")
                self.error_user.setText("INVALID URL! TRY AGAIN")
    def ok(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="container")
        title1 = str(title)
        title2 = title1.replace('class', 'id')
        soup1 = BeautifulSoup(title2, 'html.parser')
        if soup1.find(id="_35KyD6"):
            title3 = soup1.find(id="_35KyD6").get_text(strip=True)
            price = soup1.find(id="_1vC4O_3qQ9m1").get_text(strip=True)

            price2 = price.replace(',', '')
            price3 = float(price2[1:])
            self.Title.setText(title3)
            self.product_price.setText(price)
        else:
            self.errors()
            title3 = soup1.find(id="_35KyD6").get_text(strip=True)
            price = soup1.find(id="_1vC4O_3qQ9m1").get_text(strip=True)

            price2 = price.replace(',', '')
            price3 = float(price2[1:])
            PRICE = str(self.price.text())
            if self.price.text():
                if price3 <= PRICE:
                    self.sendmail()
                else:
                    self.error.setText("ERROR :")
                    self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("PLEASE INSERT THE PRICE")
    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')

            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")

    def goToMain(self):
        self.goto("main")

#----------------------------------------------------------------------------------
class hp(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("HP")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)
        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))

        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))


        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))
    def search(self):
        webbrowser.open("https://store.hp.com/in-en/default/?jumpid=ps_2rsmbqpt1c&gclid=CjwKCAiAn7L-BRBbEiwAl9UtkLCOtMk3id2JIW9OK4EHvkIcBocTvOPjC1HcBvmwKe8OSd7kc4kHaBoCgPUQAvD_BwE&gclsrc=aw.ds")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)
                if self.buttonReply == QMessageBox.Yes:
                    self.goto("hp")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("hp")
                    self.my_web.close()
                else:
                    self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")

    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(lang="en-in"))
        title1 = title.replace('class', 'id')
        soup1 = BeautifulSoup(title1, 'html.parser')
        if soup1.find(id="base"):
            title2 = soup1.find(id="base").get_text(strip=True)
            price = soup1.find(id="price").get_text(strip=True)
            price1 = price[1:]
            price2 = price1.replace(',', '')
            price3 = float(price2)
            self.Title.setText(title2)
            self.product_price.setText(price)
        else:
            self.errors()
            PRICE = str(self.price.text())
        if self.price.text():
            if price3 <= PRICE:
                self.sendmail()
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")
    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')
            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)
            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")
    def goToMain(self):
        self.goto("main")


# -----------------
class shop(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SHOP")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))

        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))

    def search(self):
        webbrowser.open(
            "https://www.shop.com/")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("shop")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("shop")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")
    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(lang="en"))
        title1 = title.replace('class', 'id')
        soup1 = BeautifulSoup(title1, 'html.parser')
        if soup1.find(id="product__title"):
            title2 = soup1.find(id="product__title").get_text(strip=True)
            price = soup1.find(id="qa-product-price js-product-price product__price product__price--lg").get_text(strip=True)
            self.Title.setText(title2)
            self.product_price.setText(price)
        else:
            self.errors()
        PRICE = str(self.price.text())
        if self.price.text():
            if price <= PRICE:
                self.sendmail()
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")
    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")

    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')
            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")

    def goToMain(self):
        self.goto("main")
#-----------------------------------

class shopclues(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SHOPCLUES")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)
        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))
        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))

    def search(self):
        webbrowser.open(
            "https://www.shopclues.com/?ef_id=CjwKCAiAn7L-BRBbEiwAl9UtkH8fWes8zcVwJeix8ynX4sNTvg05ATEvFrCR9O5nrZ0p8_3X9Ne0ExoCkl0QAvD_BwE:G:s&s_kwcid=AL!725!3!332655616938!e!!g!!shopclues&mcid=ps&utm_source=Google&utm_medium=cpc&utm_campaign=Search_Text_Exact_Brand_Shopclues")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("shopclues")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("shopclues")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")

    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(id="main_data"))
        title1 = title.replace('class', 'id')
        soup1 = BeautifulSoup(title1, 'html.parser')
        if soup1.find('h1'):
            title2 = soup1.find('h1').get_text(strip=True)
            price = soup1.find(id="f_price").get_text(strip=True)
            self.Title.setText(title2)
            self.product_price.setText(price)
        else:
            self.errors()
        PRICE = str(self.price.text())
        if self.price.text():
            if price <= PRICE:
                self.sendmail()
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")
    def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")
    def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')

            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")
    def goToMain(self):
        self.goto("main")
#-------------------------------------
class snapdeal(PageWindow):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("SNAPDEAL")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))

        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))

     def search(self):
        webbrowser.open(
            "https://www.snapdeal.com/?utm_term=469343806318_57444771733_{bidstrategy}&gclid=CjwKCAiAn7L-BRBbEiwAl9UtkCEp5GudZS8OVTYcnQBLdsF0kGzYXGLpVMTxMc3h812p3R0x9D2u9hoCCJAQAvD_BwE&utm_campaign=brand_account_brandcat_roas_ftu&utm_source=earth_sembrand&utm_medium=snapdeal")

     def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("snapdeal")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("snapdeal")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")
     def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(lang='en'))
        title1 = title.replace('class','id')
        soup1 = BeautifulSoup(title1,'html.parser')
        print("yess")
        if soup.find(itemprop="name"):
            title2 = str(soup.find(itemprop="name").get_text(strip=True))
            price = soup.find(itemprop="price").get_text(strip=True)
            self.Title.setText(title2)
            self.product_price.setText(price)

        else:
            self.errors()
        PRICE = str(self.price.text())
        if self.price.text():
            if price <= PRICE:
                self.sendmail()
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")
     def errors(self):
        self.error.setText("ERROR :")
        self.error_user.setText("INVALID URL OF THE PRODUCT! TRY AGAIN")
     def sendmail(self):
        url = self.url.text()
        URL1 = str(url)
        mail = self.mail.text()
        MAIL_USER = str(mail)
        if self.mail.text():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('d.harish0004@gmail.com', 'xuwwcthtaucrjeqk')

            subject = 'PRICE FELL DOWN '
            body = 'check out the following amazon link', URL1
            msg = f"Subject:{subject}\n\n{body}"
            server.sendmail('d.harish0004@gmail.com', MAIL_USER, msg)

            print('HEY MAIL HAS SENT CHECK OUT YOUR MAIL BOX')

            server.quit()
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("Invalid Mail id try again")

     def goToMain(self):
        self.goto("main")
class walmart(PageWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("WALMART")
        self.setGeometry(0, 0, 1000, 1000)
        button = QPushButton("", self)
        button.resize(30, 30)
        button.setStyleSheet("background-image : url(back1.png);")
        button.clicked.connect(self.goToMain)

        search = QPushButton("Search", self)
        search.move(700, 100)
        search.clicked.connect(self.search)

        urllabel = QLabel("URL :", self)
        urllabel.move(100, 95)
        urllabel.setFont(QFont('Arial', 10))

        maillabel = QLabel("MAIL ID:", self)
        maillabel.move(100, 195)
        maillabel.setFont(QFont('Arial', 10))

        pricelabel = QLabel("PRICE :", self)
        pricelabel.move(100, 295)
        pricelabel.setFont(QFont('Arial', 10))

        self.url = QLineEdit(self)
        self.url.move(150, 100)
        self.url.resize(500, 20)
        self.mail = QLineEdit(self)
        self.mail.move(150, 200)
        self.mail.resize(500, 20)
        self.price = QLineEdit(self)
        self.price.move(150, 300)
        self.price.resize(100, 20)
        okbutton = QPushButton("ok", self)
        okbutton.move(300, 350)
        okbutton.clicked.connect(self.browser)
        self.Product = QLabel("PRODUCT : ", self)
        self.Product.move(100, 400)
        self.Product.resize(150, 30)
        self.Product.setFont(QFont('Arial', 15))
        self.Title = QLabel("", self)
        self.Title.move(250, 400)
        self.Title.resize(900, 30)
        self.Title.setFont(QFont('Arial', 15))
        self.Price = QLabel("PRICE :", self)
        self.Price.move(100, 500)
        self.Price.resize(150, 30)
        self.Price.setFont(QFont('Arial', 15))
        self.product_price = QLabel("", self)
        self.product_price.move(250, 500)
        self.product_price.resize(900, 30)
        self.product_price.setFont(QFont('Arial', 15))
        self.error = QLabel("", self)
        self.error.move(100, 600)
        self.error.resize(150, 30)
        self.error.setFont(QFont('Arial', 15))
        self.error_user = QLabel("", self)
        self.error_user.move(250, 600)
        self.error_user.resize(500, 30)
        self.error_user.setFont(QFont('Arial', 15))

    def search(self):
        webbrowser.open(
            "https://www.walmart.com/")

    def browser(self):
        if self.url.text():
            URL = self.url.text()
            if validators.url(URL):
                self.my_web = QWebEngineView(self)
                self.my_web.resize(1000, 1000)
                self.my_web.load(
                    QUrl(URL))
                self.my_web.show()

                self.buttonReply = QMessageBox.question(self, 'SUMMA', "Is This The Product you Searching for?",
                                                        QMessageBox.Yes | QMessageBox.No)

                if self.buttonReply == QMessageBox.Yes:
                    self.goto("walmart")
                    self.my_web.close()
                    self.ok()
                elif self.buttonReply == QMessageBox.No:
                    self.goto("walmart")
                    self.my_web.close()
            else:
                self.errors()

        else:
            self.error.setText("ERROR :")
            self.error_user.setText("INVALID URL! TRY AGAIN")

    def ok(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        url = self.url.text()
        URL1 = str(url)
        page = requests.get(URL1, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = str(soup.find(lang="en"))
        title1 = title.replace('class', 'id')
        soup1 = BeautifulSoup(title1, 'html.parser')
        if soup1.find(id="prod-ProductTitle prod-productTitle-buyBox font-bold"):
            title2 = soup1.find(id="prod-ProductTitle prod-productTitle-buyBox font-bold").get_text(strip=True)
            price = soup1.find(id="price-group").get_text(strip=True)
            self.Title.setText(title2)
            self.product_price.setText(price)
        else:
            self.errors()
        PRICE = str(self.price.text())
        if self.price.text():
            if price <= PRICE:
                self.sendmail()
            else:
                self.error.setText("ERROR :")
                self.error_user.setText("SORRY PRICE HAS NOT FELL DOWN")
        else:
            self.error.setText("ERROR :")
            self.error_user.setText("PLEASE INSERT THE PRICE")


    def goToMain(self):
        self.goto("main")

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(0, 0, 1100, 725)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.stacked_widget =QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.m_pages = {}

        self.register(MainWindow(), "main")
        self.register(amazon(), "amazon")
        self.register(american(), "american")
        self.register(dell(), "dell")
        self.register(ebay(), 'ebay')
        self.register(flipkart(), "flipkart")
        self.register(hp(), "hp")
        self.register(shop(), "shop")
        self.register(shopclues(), "shopclues")
        self.register(snapdeal(), "snapdeal")
        self.register(walmart(), "walmart")

        self.goto("main")
    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())

app = QApplication(sys.argv)

w=Window()
w.show()
sys.exit(app.exec_())
