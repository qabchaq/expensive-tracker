balance=10000

healt = input("hey man how are you today\ntierd , fine :")
if healt.__eq__('tierd'):
    print('ok you dont go city')
elif healt.__eq__('fine'):
    print('hi! man. now you are in the city ')
    print('-----------------------------------')
print(f'you have {balance} af')
print('________________________')
class One:
    def _init_(self):
     pass


    def choose(self):

      while True:
            num  = input("What do you want?\n1: Shoes\n2: Clothes\n3: Restaurant\n")

            if num in ['1', 'shoes']:
                return 'shoes'
            elif num in ['2', 'clothes']:
                return 'clothes'
            elif num in ['3', 'restaurant']:
                return 'restaurant'

            else:
                print(" your choice wrong! Please try again.")

    def choose_country(self):

        while True:

           country = int(input("From which country?\n1: Pakistani\n2: Indian\n3: Afghani :"))
           if country in [1, 2, 3]:
                return country
           else:
              print(" Try again.")
    def menu(self):
        while True:
            menu=int(input("chooce for eat?\n 1:qabli\n 2:shinwari \n3:coffee\n 4:sandwech\n 5:pizza\n"))
            if menu in [1, 2 ,3 ,4 ,5]:
                return menu
            else:
                print('try again.')

    def buy(self, item):
         global balance

         price = int(input(f"Enter the price for {item}: "))
         if price >balance:
             print("Not enough balance! Try a lower price.")
             add = input('If you want add money?ok /no: ')
             if add == 'ok':
                 ad = int(input('enter how much want? '))
                 balance += ad
                 print(f'new balance{ balance}')
             else:
                 return False
             return True
         else:
             print(f"Buyer: {item}, Price: {price}")
             balance-=price

             print(f"Now you have {balance} money left.")

             if balance == 0:
                 print("You have no money left for today!")
                 add=input('If you want add money?ok /no: ')
                 if add=='ok':
                     ad=int(input('enter how much want? '))
                     balance+=ad
                     print(f'new balance { balance}')
                 else:
                     return False

             return True

    def today(self):


        while True:
            num  = self.choose()
            if num  is None:
                break

            if num  in ['shoes', 'clothes']:
                country = self.choose_country()
                print(f"You chose {num } from country {country}.")

            elif num in ['restaurant']:
                 menu=self.menu()

                 print(f"You chose{ num }from menu {menu}")

            con = input("Are you sure to buy? (yes/no)\n")
            if con.__eq__('yes'):
                if not self.buy(num):
                    break
            else:
                print("No purchase made.")


obj=One()
obj.today()
