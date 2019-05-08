'''
Date: 05/06/2019
Developer: Andrew Serrra
Description: Class that contains settings for the operations,
             saves the data in a file in case of server downtime.
'''
import json

class Settings:

    def __init__(self):
        # read file to get all the data that is needed
        with open("settings.txt", "r") as f:
            data = json.load(f)

            self.file_name = data["file_name"]
            self.team_names = data["team_names"]
            self.channel_access = data["channel_access"]
            self.commands_avail = data["commands_avail"]

    def setTeam(self, data_ch_name, data_text, action=None):

        return_msg = ""

        # returns false if the channel does not have access to
        # change settings
        if data_ch_name not in self.channel_access["settings"]:
            return "This channel cannot be used to change settings.\nOnly eboard has access."

        if action == "add":
            # add the new team name and save to file.
            self.team_names.append(data_text[-1])
            return_msg = "Successfully added {} from the team list.".format(data_text[-1])

        elif action == "remove":
            # remove the team name and save to file.
            self.team_names.remove(data_text[-1])
            return_msg = "Successfully removed {} from the team list.".format(data_text[-1])

        self.saveSettings()

        return return_msg

    def getFileName(self):

        return self.file_name

    def saveSettings(self):

        with open("settings.txt", "w") as text_file:
            json.dump({ "file_name": self.file_name,
                        "team_names": self.team_names,
                        "channel_access": self.channel_access,
                        "commands_avail": self.commands_avail}, text_file, indent=4)
