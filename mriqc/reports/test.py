import jinja2
from pathlib import Path

env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(searchpath=str(
                    # Path(__file__).parent / "data" / "rating-widget"
                    Path(__file__).parent / "data" / "rating-widget" / "header.tpl"
                )),
                trim_blocks=True,
                lstrip_blocks=True,
                autoescape=False,
            )

# env.get_template(str(Path(__file__).parent / "data" / "rating-widget" / "header.tpl").render())