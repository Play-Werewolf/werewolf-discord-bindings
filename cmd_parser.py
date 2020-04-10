
class Parser:
    def __init__(self, discord_bot, context, command, args):
        self.discord_bot = discord_bot
        self.context = context
        self.command = command
        self.args = args
        self.parse()

    def parse(self):
        commands = {
            "roles": self.print_roles,
            "new": self.start_new_game,
            "join": self.join_game
        }

    def print_roles(self):
        self.context.channel.send("The roles are")

    def start_new_game(self):
        """The args can be like that"""
        pass

    def check_channels(self):
        pass

    def set_channel_state(self):
        pass

    def join_game(self):
        pass

