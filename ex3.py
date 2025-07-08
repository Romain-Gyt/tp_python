def create_weather_station(localisation):
    observers = []
    temperature = 0

    def subscribe(observer_name, seuil_temp):
        observers.append((observer_name, seuil_temp))

    def unsubscribe(observer_name):
        nonlocal observers
        nouvelle_liste = []
        for obs in observers:
            nom = obs[0]
            if nom != observer_name:
                nouvelle_liste.append(obs)
        observers = nouvelle_liste

    def change_temperature(nouvelle_temp):
        nonlocal temperature
        temperature = nouvelle_temp
        notify()

    def notify():
        for observer_name, seuil_temp in observers:
            if temperature >= seuil_temp:
                print(f"{localisation} : notification envoyée à {observer_name} (température = {temperature}°C)")

    return subscribe, unsubscribe, change_temperature



quimper_subscribe, quimper_unsubscribe, quimper_change_temp = create_weather_station("quimper")

quimper_subscribe("olivier", 40)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)

quimper_change_temp(24)
quimper_change_temp(30)
quimper_change_temp(32)

quimper_unsubscribe("pierre")
quimper_change_temp(35)
