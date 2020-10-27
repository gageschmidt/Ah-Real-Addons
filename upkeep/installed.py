from pathlib import Path


# This class will be used to handle any of the various checks needed for currently installed addons
class Installed:

    @staticmethod
    # static method to check for the standard addons folder for World Of Warcraft
    def check_for_addons(text_container):
        addons_dir = Path('/Program Files (x86)/World of Warcraft/_retail_/Interface/AddOns')
        if addons_dir.is_dir():
            for sub_dir in addons_dir.iterdir():
                addon_name = sub_dir.name
                # Use names to check for addon repos?
                text_container.insert("end-1c", addon_name + '\n')
        else:
            text_container.insert("end-1c", 'No addons currently installed, '
                                            'or the default path is not being used for your WoW Installation')
