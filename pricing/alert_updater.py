from models.alert import Alert

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()
    alert.json()

if not alerts:
    print("No alerts have been created. Add an item and a alert to begin!")
