import requests

from .registry import ability


@ability(
    name="generate_html",
    description="Generate HTML code with specified page title, header, and body content",
    parameters=[
        {"name": "page_title", "description": "Title of the HTML page", "type": "string", "required": True},
        {"name": "header_content", "description": "Content for the header section", "type": "string", "required": True},
        {"name": "body_content", "description": "Content for the body section", "type": "string", "required": True}
    ],
    output_type="string"
)
async def generate_html(agent, task_id: str, page_title: str, header_content: str, body_content: str) -> str:
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{page_title}</title>
    </head>
    <body>
        <header>{header_content}</header>
        <main>{body_content}</main>
    </body>
    </html>
    """
    return html_template

@ability(
    name="generate_css",
    description="Generate CSS code based on style properties",
    parameters=[
        {"name": "style_properties", "description": "Dictionary of CSS properties and values", "type": "dict", "required": True}
    ],
    output_type="string"
)
async def generate_css(agent, task_id: str, style_properties: dict) -> str:
    css_code = "\n".join([f"{key}: {value};" for key, value in style_properties.items()])
    return css_code

@ability(
    name="generate_javascript",
    description="Generate JavaScript code for a function",
    parameters=[
        {"name": "function_name", "description": "Name of the JavaScript function", "type": "string", "required": True},
        {"name": "function_body", "description": "Body of the JavaScript function", "type": "string", "required": True}
    ],
    output_type="string"
)
async def generate_javascript(agent, task_id: str, function_name: str, function_body: str) -> str:
    js_template = f"""
    function {function_name}() {{
        {function_body}
    }}
    """
    return js_template
