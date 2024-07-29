import datetime
import sublime
import sublime_plugin


# Ctrl+Shift+, { "keys": ["ctrl+shift+,"], "command": "add_date" },
class AddDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(
            "insert_snippet",
            {
                "contents": "%s"
                % datetime.datetime.today().strftime("%d %B %Y (%A) %H:%M:%S%p")
            },
        )


# Ctrl+Shift+. { "keys": ["ctrl+shift+,"], "command": "add_time" },
class AddTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(
            "insert_snippet",
            {
                "contents": "%s"
                % datetime.datetime.today().strftime("%A, %d/%m/%Y %H:%M:%S%p")
            },
        )


# Ctrl+Shift+U { "keys": ["ctrl+shift+u"], "command": "capitalize_text" },
class CapitalizeTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                capitalized_text = selected_text.title()
                self.view.replace(edit, region, capitalized_text)
