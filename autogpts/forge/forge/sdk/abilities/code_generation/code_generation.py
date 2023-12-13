from typing import Dict

from ..registry import ability


@ability(
    name="generate_html",
    description="Generate HTML code from a dictionary of elements and attributes",
    parameters=[
        {
            "name": "elements",
            "description": "Dictionary of elements and their attributes",
            "type": "dict",
            "required": True,
        }
    ],
    output_type="string",
)
async def generate_html(agent, task_id: str, elements: Dict[str, Dict[str, str]]) -> str:
    html = ""
    for element, attributes in elements.items():
        attr_str = " ".join(f'{name}="{value}"' for name, value in attributes.items())
        html += f"<{element} {attr_str}></{element}>\n"
    return html

@ability(
    name="generate_css",
    description="Generate CSS code from a dictionary of selectors and properties",
    parameters=[
        {
            "name": "selectors",
            "description": "Dictionary of selectors and their properties",
            "type": "dict",
            "required": True,
        }
    ],
    output_type="string",
)
async def generate_css(agent, task_id: str, selectors: Dict[str, Dict[str, str]]) -> str:
    css = ""
    for selector, properties in selectors.items():
        prop_str = "\n".join(f"{name}: {value};" for name, value in properties.items())
        css += f"{selector} {{\n{prop_str}\n}}\n"
    return css

@ability(
    name="generate_js",
    description="Return the input JavaScript code",
    parameters=[
        {
            "name": "code",
            "description": "JavaScript code",
            "type": "string",
            "required": True,
        }
    ],
    output_type="string",
)
async def generate_js(agent, task_id: str, code: str) -> str:
    return code
