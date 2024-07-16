# About.py
import mesop as me

@me.page(path="/About")
def About():
  Pagestate = me.state(PageState)
  me.text("Page 2 - count:")

@me.stateclass
class PageState:
  count: int