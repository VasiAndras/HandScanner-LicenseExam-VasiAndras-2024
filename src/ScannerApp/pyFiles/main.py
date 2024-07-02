import sys
import subprocess
import re
from datetime import datetime
import os
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QStyledItemDelegate
from PyQt5 import QtCore, QtWidgets
from AddItemToDb import Ui_MainWindow as AddItemToDb_Ui_MainWindow
from AddItemToDb_validUserData import Ui_MainWindow as AddItemToDb_validUserData_Ui_MainWindow
from DbMaintenance_query import Ui_MainWindow as DbMaintenance_query_Ui_MainWindow
from DbMaintenance import Ui_MainWindow as DbMaintenance_Ui_MainWindow
from InsertNewUser_GDPR import Ui_MainWindow as InsertNewUser_GDPR_Ui_MainWindow
from InsertNewUser import Ui_MainWindow as InsertNewUser_Ui_MainWindow
from MainPage import Ui_MainWindow as MainPage_Ui_MainWindow
from database_manager import Database  

class MyApp_AddItemToDb(QMainWindow, AddItemToDb_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user_code = None
        self.addItemToDb_backButton.clicked.connect(self.close_window)
        self.addItemToDb_searchUserButton.clicked.connect(self.capture)

    def open_AddItemToDb_validUserData(self):
        self.open_AddItemToDb_validUserData_window = MyApp_AddItemToDb_validUserData()
        self.open_AddItemToDb_validUserData_window.set_code(self.user_code)
        self.open_AddItemToDb_validUserData_window.show()

    def capture(self):
        self.user_code = self.addItemToDb_codeInput.text()
        self.user_code = self.user_code.strip()
        file_path = "Database/database.json"
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        result = False
        for user in data['users']:
            if user['usercode'] == self.user_code:
                result = True

        if result:
            print(f"User code {self.user_code} is in the JSON file.")
            self.open_AddItemToDb_validUserData()
        else:
            print(f"User code {self.user_code} is not in the JSON file.")
            QMessageBox.warning(self, "Invalid Data", "User code is invalid or is'nt saved to database!")

    def close_window(self):
        self.close()

class MyApp_AddItemToDb_validUserData(QMainWindow, AddItemToDb_validUserData_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.local_code = "None"
        self.AddItemToDb_backButton.clicked.connect(self.close_window)
        self.AddItemToDb_captureLHandButton.clicked.connect(self.captureLeft)
        self.AddItemToDb_captureRHandButton.clicked.connect(self.captureRight)
        
    def set_code(self, code):
        self.local_code = code
        self.AddItemToDb_userCodeLabel.setText(self.local_code)

    def get_num_pics(self, filename, actual_user_code, hand):
        with open(filename, 'r') as file:
            json_data = json.load(file)
            
        users_data = json_data.get('users', [])
        for user in users_data:
            if user["usercode"] == actual_user_code:
                ordnr = user["pictures"].get(hand, None)
        return ordnr

    def update_database(self, filename, actual_user_code, hand):
        with open(filename, 'r') as file:
            json_data = json.load(file)

        general_data = json_data.get('general', {})
        general_data['totalImageCount'] += 1
        users_data = json_data.get('users', [])
        for user in users_data:
            if user["usercode"] == actual_user_code:
                user["pictures"][hand] += 1
                break
        
        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)
            
    def captureLeft(self):
        file_path = "Database/database.json"
        ordnr = self.get_num_pics(file_path, self.local_code, "leftHand")
        if ordnr is not None:
            ordnr = str(ordnr)
            command = ["python", "capture.py", self.local_code, "L", ordnr]
            try:
                subprocess.run(command, check=True)
                self.update_database(file_path, self.local_code, "leftHand")
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print(f"No left hand picture data found for user {self.local_code}")

    def captureRight(self):
        file_path = "Database/database.json"
        ordnr = self.get_num_pics(file_path, self.local_code, "rightHand")
        if ordnr is not None:
            ordnr = str(ordnr)
            command = ["python", "capture.py", self.local_code, "R", ordnr]
            try:
                subprocess.run(command, check=True)
                self.update_database(file_path, self.local_code, "rightHand")
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print(f"No right hand picture data found for user {self.local_code}")
    
    def close_window(self):
        self.close()

class MyApp_DbMaintenance_query(QMainWindow, DbMaintenance_query_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.DbMaintenance_query_backButton.clicked.connect(self.close_window)
        self.search_results = []

    def set_results(self, search_results):
        self.search_results = search_results
        self.setup_model()
        
    def close_window(self):
        self.close()

    def setup_model(self):
        data = []
        file_path = "Database/database.json"
        data = self.read_json_file(file_path, self.search_results)
        print(data)
        model = MyTableModel(data)
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 100)  # User Code
        self.tableView.setColumnWidth(1, 150)  # Legal Name
        self.tableView.setColumnWidth(2, 100)  # Birth Day
        self.tableView.setColumnWidth(3, 100)  # Pictures
        self.tableView.setColumnWidth(4, 100)  # Copy Button
        self.tableView.setItemDelegateForColumn(4, ButtonDelegate(self))

    def read_json_file(self, filename, search_results):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        
        users_data = json_data.get('users', [])
        data = []
        for user in users_data:
            if user['usercode'] in search_results:
                data.append({
                    "usercode": user.get("usercode", ""),
                    "legalName": user.get("legalName", ""),
                    "birthDay": user.get("birthDay", ""),
                    "pictures": {
                        "rightHand": user["pictures"].get("rightHand", 0),
                        "leftHand": user["pictures"].get("leftHand", 0)
                    }
                })
        return data

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(MyTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            item = self._data[row]
            if column == 0:
                return item["usercode"]
            elif column == 1:
                return item["legalName"]
            elif column == 2:
                return item["birthDay"]
            elif column == 3:
                return f'RH: {item["pictures"]["rightHand"]}, LH: {item["pictures"]["leftHand"]}'

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 5

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                headers = ["User Code", "Legal Name", "Birth Day", "Pictures", "Copy"]
                return headers[section]

class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)
        self.parent = parent


    def editorEvent(self, event, model, option, index):
        if index.column() == 4 and event.type() == QtCore.QEvent.MouseButtonRelease:
            self.copy_usercode(index)
        return super(ButtonDelegate, self).editorEvent(event, model, option, index)

    def copy_usercode(self, index):
        usercode = index.model()._data[index.row()]["usercode"]
        clipboard = QApplication.clipboard()
        clipboard.setText(usercode)
        QMessageBox.information(None, "Copied", f"Usercode {usercode} copied to clipboard.")


class MyApp_DbMaintenance(QMainWindow, DbMaintenance_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AddItemToDb_backButton.clicked.connect(self.close_window)
        self.AddItemToDb_searchButton.clicked.connect(self.search)

    def search(self):
        self.search_term = self.AddItemToDb_nameInput.text()
        self.search_term = self.search_term.strip()
        self.local_codes = []
        file_path = "Database/database.json"
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        result = False
        for user in data['users']:
            if user['usercode'] == self.search_term or self.search_term.lower() in user['legalName'].lower().strip():
                result = True
                self.local_codes.append(user['usercode'])

        if result:
            print(f"{self.search_term} is in the JSON file.")
            print(self.local_codes)
            self.open_MyApp_DbMaintenance_query()
        else:
            print(f"{self.search_term } is not in the JSON file.")
            QMessageBox.warning(self, "Invalid Data", "There is no match for this name or user code!")

    def open_MyApp_DbMaintenance_query(self):
        self.open_MyApp_DbMaintenance_query_window = MyApp_DbMaintenance_query()
        self.open_MyApp_DbMaintenance_query_window.set_results(self.local_codes)
        self.open_MyApp_DbMaintenance_query_window.show()

    def close_window(self):
        self.close()

class MyApp_InsertNewUser_GDPR(QMainWindow, InsertNewUser_GDPR_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.local_code = "None"
        self.local_name = "None"
        self.local_bday = "None"
        self.InsertNewUser_GDPR_backButton.clicked.connect(self.close_window)
        self.InsertNewUser_GDPR_agreeAndSignButton.clicked.connect(self.sign_window)

    def set_code(self, code):
        self.local_code = code
        
    def set_name(self, name):
        self.local_name = name
        
    def set_birthday(self, bday):
        self.local_bday = bday

    def sign_window(self):
        command = [
        'python3', 'Sign.py',
        '-uc', str(self.local_code),
        '-ln', str(self.local_name),
        '-bd', str(self.local_bday)
        ]
        try:
            subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while running Sign.py: {e}")

        db = Database()
        directory = self.local_code + "_db"
        parent_dir = "Database/"
        path = os.path.join(parent_dir, directory) 
        os.mkdir(path) 
        print("Directory '% s' created" % directory) 

        def open_insert_user(self):
            self.insert_user_window = MyApp_InsertNewUser()
            self.insert_user_window.show()

        def generate_gdpr_pdf(self):
            command = [
            'python3', 'generate_gdpr_pdf.py',
            '-uc', str(self.local_code),
            '-ln', str(self.local_name),
            '-bd', str(self.local_bday)
            ]
            try:
                subprocess.run(command, capture_output=True, text=True, check=True)
                gdpr_file = "GDPR_certificate_" + self.local_name + self.local_code + "_" + ".pdf"
                db.add_user(self.local_code, self.local_name, self.local_bday, path, gdpr_file)
                self.close_window()
            except subprocess.CalledProcessError as e:
                print(f"Error while running generate_gdpr_pdf.py: {e}")

        generate_gdpr_pdf(self)

    def close_window(self):
        self.close()

class MyApp_InsertNewUser(QMainWindow, InsertNewUser_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InserNewUser_backButton.clicked.connect(self.close_window)
        self.InserNewUser_insertUserButton.clicked.connect(self.try_save_user_data)
        
    def close_window(self):
        self.close()
        
    def try_save_user_data(self):
        name = self.InserNewUser_nameInput.text()
        bday = self.InserNewUser_bdayInput.text()

        full_name = name

        def real_name_detector(name):
            if len(name) < 2 or len(name) > 50:
                return False
            
            if not re.match(r"^[a-zA-Z\s'-]+$", name):
                return False
            
            if re.search(r"[-'\s]{2,}", name):
                return False
            
            if not name[0].isalpha() or not name[-1].isalpha():
                return False

            if not name[0].isalpha() or not name[-1].isalpha():
                return False
            
            words = name.split()
            if len(words) < 2:
                return False

            return True

        def valid_birthdate_detector(bday):

            try:
                birthdate = datetime.strptime(bday, "%Y.%m.%d.")
                if birthdate > datetime.now():
                    return False
                
                return True
            except ValueError:
                return False

        def generate_code(name, birthdate):
            initials = ''.join(word[0].upper() for word in name.split())
            birth_year = birthdate.split('.')[0][-2:]
            birth_month = birthdate.split('.')[1]
            birth_day = birthdate.split('.')[2]
            code = initials + birth_year + birth_month + birth_day
            return code

        is_valid_name = real_name_detector(name)
        is_valid_birthdate = valid_birthdate_detector(bday)
        print(f"Name: {name}, is valid: {is_valid_name}")
        print(f"Birth date: {bday}, is valid: {is_valid_birthdate}")
        if not is_valid_name or not is_valid_birthdate:
            QMessageBox.warning(self, "Invalid Data", "The entered name or birthdate is invalid.")
        else:
            code = generate_code(name, bday)
            self.insert_user_GDPR_window = MyApp_InsertNewUser_GDPR()
            self.insert_user_GDPR_window.set_code(code)
            self.insert_user_GDPR_window.set_name(full_name)
            self.insert_user_GDPR_window.set_birthday(bday)
            self.insert_user_GDPR_window.show()
            self.close()

class MyApp_MainPage(QMainWindow, MainPage_Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.MainPage_insertUserButton.clicked.connect(self.open_insert_user)
        self.MainPage_capturePhotoButton.clicked.connect(self.open_add_item_to_db)
        self.MainPage_databaseMaintananceButton.clicked.connect(self.open_db_maintenance)

    def open_insert_user(self):
        self.insert_user_window = MyApp_InsertNewUser()
        self.insert_user_window.show()

    def open_add_item_to_db(self):
        self.add_item_to_db_window = MyApp_AddItemToDb()
        self.add_item_to_db_window.show()

    def open_db_maintenance(self):
        self.db_maintenance_window = MyApp_DbMaintenance()
        self.db_maintenance_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_MainPage = MyApp_MainPage()
    window_MainPage.show()
    sys.exit(app.exec_())

