import os, shutil

# nama program
program_name = 'HTDoxer'
author = 'github.com/powzee'

# isi path dibawah
path = 'C:\\xampp\\htdocs\\'
xampp_mysql_path = 'C:\\xampp\\mysql\\bin\\'
output_backup = f'D:\\{program_name}\\'
        
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

class HTDoxer():
    def __init__(self):
        self.listdir = os.listdir(path)
        self.listdir = [i for i in self.listdir if '.' not in i]
        self.listdir = [i for i in self.listdir if i not in ['dashboard','img','webalizer','xampp','test']]
    def add_path(self):
        if xampp_mysql_path not in os.environ['PATH']:
            os.environ['PATH'] += f';{xampp_mysql_path}'
        else:
            pass
    def make_backup_folder(self):
        if not os.path.exists(f'{output_backup}'):
            os.mkdir(f'{output_backup}')
        else:
            pass    
    def backup_database(self, db_name, folder_name):
        try:
            os.system(f'mysqldump -u root {db_name} > {output_backup}{folder_name}\\database\\{db_name}.sql')
        except:
            print('XAMPP tidak aktif atau XAMPP MySQL tidak tersedia di path sistem!')
    def xampp_dir(self):
        num = 0
        for i in self.listdir:
            num += 1
            print(f'{num}. {i}')
    def backup(self):
        self.add_path()
        print('='*25 + f' {program_name.upper()} ' + '='*25)
        print('List Folder di htdocs kamu:')
        self.xampp_dir()
        print('='*59)
        print('Created by: ' + author)
        print('='*59)
        folder_index = int(input('Pilih Folder: '))
        database_name = input('Nama Database: ')
        folder_name = self.listdir[folder_index-1]
        print('='*59)
        if folder_name not in os.listdir(path):
            print('Folder tidak ada!')
        else:
            print(f'Sedang mem-backup folder {folder_name}...')
            self.make_backup_folder()
            if folder_name in os.listdir(output_backup):
                shutil.rmtree(f'{output_backup}{folder_name}')
            shutil.copytree(f'{path}{folder_name}', f'{output_backup}{folder_name}')
            os.mkdir(f'{output_backup}{folder_name}\\database')
            print(f'Sedang mem-backup database {database_name} ...')
            self.backup_database(database_name, folder_name)
            print('Backup Selesai')

if __name__ == '__main__':
    htdoxer = HTDoxer()
    htdoxer.backup()
