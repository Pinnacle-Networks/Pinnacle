from pinnacle import pinnacle
from templates.agent.help import add_app_from_template

db = pinnacle()
add_app_from_template(db, "./agent_template_simple")
