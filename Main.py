import mesop as me
from routes import NavBar


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://google.github.io"]
  ),
  path="/",
)

def Main():
    NavBar.NavBar()
    me.text('Main')
    
