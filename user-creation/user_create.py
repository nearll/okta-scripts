import random, json, uuid 

class UserCreation:

    def __init__(self):
        self.first_names = ('Wendy', 'Louis', 'Nick', 'Rick', 'Deckard', 'George', 
        'Erin', 'Justin', 'Steven', 'Richard', 'Adams', 'Jennifer', 'Austin')

        self.last_names = ('Smith', 'Adams', 'Johnson', 'Shaffer') 

    def generate_first_name(self):
        return random.choice(self.first_names)

    def generate_last_name(self):
        return random.choice(self.last_names)

    def generate_profile(self):
        first_name = self.generate_first_name()
        last_name = self.generate_last_name()
        profile_object = {}
        profile_object["firstName"] = first_name
        profile_object["lastName"] =  last_name
        profile_object["email"] = first_name + last_name + "@gmail.com"
        profile_object["login"] = first_name + last_name + "@gmail.com"
        profile_object["mobilePhone"] = "231-313-1313"
        return profile_object

    def generate_credentials(self):
        credentials_object = {}
        password_object = {}
        password_object["value"] = uuid.uuid4().hex
        credentials_object["password"] = password_object
        return credentials_object

    def populate_input_file(self, json_object):
        input_file = open("users.txt", "w+")
        input_file.write("[")
        input_file.write(json.dumps(json_object))
        input_file.write("]")
        input_file.close()
        
    def populate_users_file(self, json_object):
        input_file = open("users_login.txt", "w+")
        input_file.write(json.dumps(json_object))
        input_file.close()


def main():
    creation = UserCreation()
    activation_data = {}
    testing_data = {}
    full_activation_data = ""
    full_testing_data = ""
    for i in range(10):
        activation_data["profile"] = creation.generate_profile()
        activation_data["credentials"] = creation.generate_credentials()
        testing_data["login"] = activation_data["profile"]["login"]
        testing_data["password"] = activation_data["credentials"]["password"]["value"]

    creation.populate_input_file(activation_data)
    creation.populate_users_file(testing_data)


    print(json.dumps(activation_data))
    print(json.dumps(testing_data))

if __name__ == "__main__":
    main()

