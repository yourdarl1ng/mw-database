import os


# function to make a new database
def make_db(name):
    # lists local folder content
    local_folder_content = os.listdir()
    # looks if the database you are looking for exists
    if str(name) in local_folder_content:
        # if your db wasn't found this will be printed out
        return print("Database with this name already exists!")
    else:
        # makes a new db file
        db_name = (str(name) + ".py")
        with open(db_name, "w+") as db:
            db.close()
            return print("New database made!")


# read info from database
def read_db(name, print_content=False):
    try:
        db_name = (str(name) + ".py")
        # opens your desired database
        with open(str(db_name), "r") as db:

            # reads db content
            db_content = db.read()

            if print_content:
                print(str(db_content))
            # closes the db
            db.close()
            return db_content
    except:
        print("Failed to get db content")


def write_entry(name, user_name, user_id, user_age, user_bio, user_adinfo):


    # looks if the database you are looking for exists


    try:
        db_name = (str(name) + ".py")

        # opens your desired database

        with open(str(db_name), "r") as db:
            # reads db content

            db_content = db.read()
            # makes a new dictionary for the user

            db.close()

        db = open(str(db_name), "w")
        user_dict = {
            "Username": str(user_name),
            "UID": int(user_id),
            "Age": int(user_age),
            "Biography": str(user_bio),
            "Other": str(user_adinfo)
        }

        db_to_write = str(db_content) + "\n" + str(user_name) + " = " + str(user_dict)
        # writes user's data to your db
        db.write(str(db_to_write))
        print("new entry written to db")
        db.close()
    except:
        print("Failed to write to db")

#read desired user's info

def read_user_info(name, username):
    try:
        db_name = (str(name) + ".py")
        db = open(str(db_name), "r")
        db_content = db.read()
        db.close()
        info1 = str(db_content.split(f"{username} = "))
        info2 = info1.split("}")
        info3 = info2[0].split("{")
        data = info3[1]



        return data
    except:
        return print("Failed to get desired user's info")