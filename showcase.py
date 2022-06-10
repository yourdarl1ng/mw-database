#imports mw_database library
from mw_database import *
#makes a new database
make_db(name="my new db")
#adds 4 new users to the database
write_entry(name="my new db", user_name="darling", user_id=1, user_age=21, user_bio="This is a bio", user_adinfo="some other info")
write_entry(name="my new db", user_name="darling2", user_id=2, user_age=21, user_bio="This is a bio", user_adinfo="some other info")
write_entry(name="my new db", user_name="darling3", user_id=3, user_age=27, user_bio="This is a bio", user_adinfo="some other info")
write_entry(name="my new db", user_name="darling4", user_id=4, user_age=25, user_bio="This is a bio", user_adinfo="some other info")

#returns info of a user
user_info = read_user_info(name="my new db", username="darling")
print(str(user_info))
