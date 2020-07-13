import pandas as pd
from os import system

class App:
    def __init__(self):
        try:
            self.data = pd.read_csv('data.csv')
        except:
            df = pd.DataFrame(
                columns = ['website', 'email_address', 'password', 'usage']
            )
            df.to_csv('data.csv', index=False)
            self.data = pd.read_csv('data.csv')
        self.footer = 'Follow me on Twitter @ejzilba. Have a nice day!\n\n'
        self.start()
    def start(self):
        while True:
            system('cls')
            print(f'{self.footer}')
            print(
                'Manage you accounts NOW!\n',
                '1 View existing accounts\' details.',
                '2 Add new account.',
                '3 Find account using email address.',
                '4 Edit information of existing accounts.',
                '5 Remove an account.',
                '6 Exit',
                sep='\n\t'
            )
            try:
                query = int(input('\n\t_ '))
            except ValueError as e:
                continue
            if query == 1:
                self.view()
            elif query == 2:
                self.append()
            elif query == 3:
                self.find()
            elif query == 4:
                self.modify()
            elif query == 5:
                self.remove()
            elif query == 6:
                system('cls')
                print('Thank you for using this app.', self.footer, sep='\n')
                break
    def find(self):
        system('cls')
        print(
            self.footer,
            'Find account ...',
            sep=''
        )
        had_found, index = self.search()
        if had_found:
            print('\n', self.data.iloc[index, :], sep='', end='\n\n')
            system('pause')
            return
        print('!not_found')
        system('pause')
    def append(self):
        system('cls')
        print(
            self.footer,
            'Add new account ...\n',
            sep=''
        )
        website = input('\tWebsite:\t')
        email_address = input('\tEmail Address:\t')
        password = input('\tPassword:\t')
        usage = input('\tUsage:\t\t')
        system('cls')
        print(self.footer)
        print(
            'The following data will be added to the database!\n',
            f'Website:\t{website}',
            f'Email Address:\t{email_address}',
            f'Password:\t{password}',
            f'Usage:\t\t{usage}',
            sep='\n\t'
        )
        decision = ''
        print('\nDo you want to continue? <Y/N>')
        while decision not in ['y',  'n']:
            decision = input('\t_ ').lower()
        if decision == 'y':
            new_data = pd.DataFrame([[website, email_address, password, usage]],
                columns=self.data.columns)
            self.data = self.data.append(new_data, ignore_index=True)
            self.data.to_csv('data.csv', index=False)
            print('\nData has been added to the database.')
        elif decision == 'n':
            print('\nAdding data has been cancelled.')
        system('pause')
    def view(self):
        system('cls')
        print(
            self.footer,
            'Account List\n',
            sep=''
        )
        if self.data.empty:
            print('No account is found!\n')
        else:
            print(self.data, end='\n\n')
        system('pause')
    def remove(self):
        system('cls')
        print(
            self.footer,
            'Remove an account ... ',
            sep=''
        )
        had_found, index = self.search()
        if had_found:
            print('\nDo you want to continue? <Y/N>')
            decision = ''
            while decision not in ['y',  'n']:
                decision = input('\t_ ').lower()
            if decision == 'y':
                self.delete(index)
                self.data.to_csv('data.csv', index=False)
                print('Data has been successfully removed!')
            elif decision == 'n':
                print('\nDeleting data has been cancelled.')
        else:
            print('!Please enter a valid email address!')
        system('pause')
    def modify(self):
        system('cls')
        print(
            self.footer,
            'Modifying accounts ...',
            sep=''
        )
        had_found, index = self.search()
        if had_found:
            info = dict(self.data.iloc[index, :])
            self.delete(index)
            print('Fill out the following info. If you don\'t want to change some info put \'NA\'')
            for key in info:
                if (new_info := input('\t'+key+': _ ')) != 'NA':
                    info[key] = [new_info]
            try:
                info = pd.DataFrame(data=info)
            except ValueError:
                print('Data was left unmodified!')
                system('pause')
                return
            print('\nDo you want to continue? <Y/N>')
            decision = ''
            while decision not in ['y',  'n']:
                decision = input('\t_ ').lower()
            if decision == 'y':
                self.data = self.data.append(info, ignore_index=True)
                self.data.to_csv('data.csv', index=False)
                print('\nData has been modified.')
            elif decision == 'n':
                print('\nModifying data has been cancelled.')
        else:
            print('!Account not found!')
        system('pause')
    def search(self):
        found = False
        index = 0
        email_address = self.data.iloc[:, 1].values
        key = input('Enter the email address of the account you want to remove:\n\t_ ')
        while not found:
            if index >= len(email_address):
                break

            if email_address[index] == key:
                found = True
                break
            index += 1
        return found, index
    def delete(self, index):
        self.data.drop([index], inplace=True)

if __name__ == '__main__':
    app = App()
