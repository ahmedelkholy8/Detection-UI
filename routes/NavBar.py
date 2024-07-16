import mesop as me
from routes import About


@me.stateclass
class State:
  sidenav_open: bool


def on_click(e: me.ClickEvent):
  s = me.state(State)
  s.sidenav_open = not s.sidenav_open


SIDENAV_WIDTH = 200

def NavBar():
  state = me.state(State)
  with me.sidenav(
    opened=state.sidenav_open, style=me.Style(width=SIDENAV_WIDTH,background = 'green')
  ):
    me.text("Inside sidenav")
    me.button("Navigate to About", on_click=gotopage)

  with me.box(
    style=me.Style(
      margin=me.Margin(left=SIDENAV_WIDTH if state.sidenav_open else 0),
    ),
  ):
    with me.content_button(on_click=on_click):
      me.icon("menu")

def gotopage(e: me.ClickEvent):
    Pagestate = me.state(About.PageState)
    Pagestate.count += 1
    me.navigate("/About")