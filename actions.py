# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from corona_cases import Corona_cases
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

"""
class ActionCasesIndia(Action):

    def name(self) -> Text:
        return "action_cases_India"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.worldometers.info/coronavirus/country/india/"

        cases=Corona_cases(url)
        dispatcher.utter_template('utter_cases',tracker,confirm=cases[0],deceased=cases[1],recovered=cases[2])

        return []
"""

class ActionCasesWorld(Action):

    def name(self) -> Text:
        return "action_world_cases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = "https://www.worldometers.info/coronavirus/"

        loc=tracker.get_slot("country")
        new_url= url+"country/"+loc

        cases=Corona_cases(new_url)
        dispatcher.utter_template('utter_world_cases',tracker,Country=loc,confirm=cases[0],deceased=cases[1],recovered=cases[2])

        return []

class ActionCasesStates(Action):

    def name(self) -> Text:
        return "action_state_cases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url1 = "https://www.worldometers.info/coronavirus/usa/"

        loc1=tracker.get_slot("state")
        new_url1= url1+loc1

        cases1=Corona_cases(new_url1)
        dispatcher.utter_template('utter_state_cases',tracker,State=loc1,confirm=cases1[0],deceased=cases1[1],recovered=cases1[2])

        return []

class ActionTotalCases(Action):

    def name(self) -> Text:
        return "action_total_cases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url2 = "https://www.worldometers.info/coronavirus/"

        cases1=Corona_cases(url2)
        dispatcher.utter_template('utter_total_cases',tracker,confirm=cases1[0],deceased=cases1[1],recovered=cases1[2])

        return []







