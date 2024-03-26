from autogpt.core.ability.builtins.create_new_ability import CreateNewAbility
from autogpt.core.ability.builtins.query_language_model import QueryLanguageModel
from autogpt.core.ability.builtins.generate_web_code import GenerateWebCode

BUILTIN_ABILITIES = {
    QueryLanguageModel.name(): QueryLanguageModel,
    GenerateWebCode.name(): GenerateWebCode,
}

__all__ = [
    "BUILTIN_ABILITIES",
    "CreateNewAbility",
    "QueryLanguageModel",
    "GenerateWebCode",
]
