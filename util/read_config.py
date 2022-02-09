import configparser


class ReadConfig(object):
    def __init__(self, filepath=None, section=None) -> None:
        if filepath == None:
            filepath = r'config\reg_config.ini'
        if section == None:
            self.section = 'RegisterElement'
        else:
            self.section = section
        self.cf = self.load_ini(filepath)

    def load_ini(self, filepath):
        cf = configparser.ConfigParser()
        cf.read(filepath)
        return cf

    def get_value(self, key):
        return self.cf.get(self.section, key)


# if __name__ == "__main__":
#     readini = ReadConfig()
#     print(readini.get_value('user_name'))
