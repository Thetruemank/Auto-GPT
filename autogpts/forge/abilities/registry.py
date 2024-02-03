import requests

from .code_generation import generate_css, generate_html, generate_javascript


class AbilityRegister:
    def __init__(self, agent):
        self.agent = agent
        self.abilities = {}
        self._register_abilities()

    def _register_abilities(self):
        self.register_ability(generate_html)
        self.register_ability(generate_css)
        register_ability(generate_javascript)

    def register_ability(self, ability_func):
        ability_details = ability_func.ability_details
        if ability_details['name'] not in self.abilities:
            self.abilities[ability_details['name']] = ability_func

    def list_abilities_for_prompt(self):
        return [details for name, details in self.abilities.items()]

    def run_ability(self, ability_name, *args, **kwargs):
        if ability_name in self.abilities:
            return self.abilities[ability_name](*args, **kwargs)
        else:
            raise ValueError(f"Ability {ability_name} not registered.")

# Unit tests covering all edge cases and scenarios for AbilityRegister modifications
