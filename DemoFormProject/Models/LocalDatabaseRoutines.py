"""
Used structures and classes
"""
from os import path
import json
import pandas as pd

def create_LocalDatabaseServiceRoutines():
    return LocalDatabaseServiceRoutines()

class LocalDatabaseServiceRoutines(object):
    def __init__(self):
        self.name = 'Data base service routines'
        self.index = {}
        self.UsersDataFile = path.join(path.dirname(__file__), '..\\static\\Data\\users.csv')

# -------------------------------------------------------
# Read users data into a dataframe
# -------------------------------------------------------
    def ReadCSVUsersDB(self):
        df = pd.read_csv(self.UsersDataFile)
        return df

# -------------------------------------------------------
# Saves the DataFrame (input parameter) into the users csv
# -------------------------------------------------------
    def WriteCSVToFile_users(self, df):
        df.to_csv(self.UsersDataFile, index=False)

# -------------------------------------------------------
# Check if username is in the data file
# -------------------------------------------------------
    def IsUserExist(self, UserName):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        df = df.set_index('username')
        return (UserName in df.index.values)

# -------------------------------------------------------
# return boolean if username/password pair is in the DB
# -------------------------------------------------------
    def IsLoginGood(self, UserName, Password):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        df=df.reset_index()
        selection = [UserName]
        df = df[pd.DataFrame(df.username.tolist()).isin(selection).any(1)]

        df = df.set_index('password')
        return (Password in df.index.values)
     
# -------------------------------------------------------
# Add a new user to the DB
# -------------------------------------------------------
    def AddNewUser(self, User):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        dfNew = pd.DataFrame([[User.FirstName.data, User.LastName.data, User.PhoneNum.data, User.EmailAddr.data, User.username.data, User.password.data]], columns=['FirstName', 'LastName', 'PhoneNum', 'EmailAddr',  'username', 'password'])
        dfComplete = df.append(dfNew, ignore_index=True)
        self.WriteCSVToFile_users(dfComplete)


        """
        
    def ReadUsersDB(self):
        users_db = path.join(path.dirname(__file__), '..\\static\\Data\\users.json')

        try:
            with open(users_db, 'r') as usersfile:  
                s = json.load(usersfile)
                x = json.loads(s)
            
                df = pd.DataFrame.from_dict(x)

        except:
            Data = {
                    'firstname': ['Teacher'],
                    'lastname': ['Tichonet'],
                    'phone': ['No-Phone'],
                    'email': ['No-Email'],
                    'username': ['Tichonet'],
                    'password': ['123456']
                    }
            df = pd.DataFrame(Data, columns=['firstname', 'lastname', 'phone',  'email', 'username', 'password'])

        finally: 
            return df


# -------------------------------------------------------
# Saves the DataFrame (input parameter) into the json's
# Users database
# -------------------------------------------------------
    def WriteToFile_users(self, df):
        users_db = path.join(path.dirname(__file__), '..\\static\\Data\\users.json')

        with open(users_db, 'w') as usersfile:  
            json.dump(df.to_json(), usersfile, indent=4 , sort_keys=True)


"""
