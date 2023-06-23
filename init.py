from dotenv import dotenv_values
from sample import notify


config = dotenv_values(".env")
notify.init_config(notify, config=config)

notify.smtp("Subject 1", "new messaage", "alibizumagaliev9@gmail.com")




