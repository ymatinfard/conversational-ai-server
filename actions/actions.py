from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your order has been placed. It will arrive soon.")
        return [None]

class ActionCheckOrderStatus(Action):
    def name(self) -> Text:
        return "action_check_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your order is being prepared and will be delivered shortly.")
        return []

class ActionCancelOrder(Action):
    def name(self) -> Text:
        return "action_cancel_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Your order has been cancelled.")
        return []

class ActionStoreFeedback(Action):
    def name(self) -> Text:
        return "action_store_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Thank you for your feedback!")
        return []

class ActionOrderConfirmation(Action):
    def name(self) -> Text:
        return "action_order_confirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get all slot values
        address = tracker.get_slot("address")
        food_order = tracker.get_slot("food_order")
        payment_method = tracker.get_slot("payment_method")
        
        # Format the food order list for better readability
        if isinstance(food_order, list):
            formatted_food = ", ".join(food_order)
        else:
            formatted_food = food_order
        
        # Create a formatted confirmation message
        confirmation_message = (
            f"Great! I've confirmed your order. Here's a summary of your order details:\n\n"
            f"📦 Food items: {formatted_food}\n"
            f"📍 Delivery address: {address}\n"
            f"💳 Payment method: {payment_method}\n\n"
            f"Your order has been placed and will be delivered soon. Thank you for ordering with us!"
        )
        
        dispatcher.utter_message(text=confirmation_message)
        return []