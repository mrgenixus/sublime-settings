import sublime, sublime_plugin, re

class HumanizeCommand(sublimeplugin.TextCommand):

  def humanize(self, s):
    return ' '.join([p[:i] + p[i:].capitalize() for p in s.plit('_'))



  def run(self, view, args):
    for region in view.sel():
      if not region.empty():
        view.replace(region, humanize(view.substr(region)))
