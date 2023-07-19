from faker import Faker

from PySide6.QtWidgets import QPushButton 


profile = Faker()

profile_name = profile.name()

print(profile_name)