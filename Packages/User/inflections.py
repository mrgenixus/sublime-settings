import sublime, sublime_plugin, re


def humanize(s):
  return re.sub('_id$', '', s).replace('_', ' ').capitalize()

def titleize(s):
  return humanize(s).title()

def underscore(word):
  return  re.sub('[^A-Z^a-z^0-9^\/]+', '_', \
          re.sub('([a-z\d])([A-Z])', '\\1_\\2', \
          re.sub('([A-Z]+)([A-Z][a-z])', '\\1_\\2', re.sub('::', '/', word)))).lower()

class HumanizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    v = self.view
    for region in v.sel():
      if not region.empty():
        sel = v.substr(region)
        v.replace(edit, region, humanize(sel))


class TitleizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    v = self.view
    for region in v.sel():
      if not region.empty():
        sel = v.substr(region)
        v.replace(edit, region, titleize(sel))
