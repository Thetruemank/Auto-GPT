import logging

from autogpt.core.ability.base import (Ability, AbilityConfiguration,
                                       AbilityResult)
from autogpt.core.plugin.simple import PluginLocation, PluginStorageFormat
from autogpt.core.utils.json_schema import JSONSchema


class GenerateWebCode(Ability):
    default_configuration = AbilityConfiguration(
        location=PluginLocation(
            storage_format=PluginStorageFormat.INSTALLED_PACKAGE,
            storage_route="autogpt.core.ability.builtins.GenerateWebCode",
        ),
    )

    description: str = "Generate HTML, CSS, or JavaScript code based on specified requirements."

    parameters: dict[str, JSONSchema] = {
        "code_type": JSONSchema(
            description="The type of code to generate (HTML, CSS, JavaScript).",
            type=JSONSchema.Type.STRING,
            required=True,
            enum=["HTML", "CSS", "JavaScript"],
        ),
        "content_requirements": JSONSchema(
            description="A description of what the generated code should achieve.",
            type=JSONSchema.Type.STRING,
            required=True,
        ),
    }

    async def __call__(
        self,
        logger: logging.Logger,
        code_type: str,
        content_requirements: str,
    ) -> AbilityResult:
        if code_type == "HTML":
            generated_code = f"<html><body>{content_requirements}</body></html>"
        elif code_type == "CSS":
            generated_code = f"body {{ {content_requirements} }}"
        elif code_type == "JavaScript":
            generated_code = f"function myFunction() {{ // {content_requirements} }}"
        else:
            generated_code = "Unsupported code type."
        
        return AbilityResult(
            success=True,
            data={"generated_code": generated_code},
            message="Web code generated successfully."
        )
