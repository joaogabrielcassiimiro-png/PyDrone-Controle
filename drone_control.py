import asyncio
import keyboard
from bleak import BleakScanner, BleakClient

RX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

def pacote(roll=127, pitch=127, yaw=127, throttle=127, button=0):
    return bytes([
        0,
        roll,
        pitch,
        yaw,
        throttle,
        button,
        0,
        0
    ])

async def main():

    print("Procurando pyDrone...")

    devices = await BleakScanner.discover()

    drone = None

    for d in devices:
        if d.name == "pyDrone":
            drone = d
            break

    if not drone:
        print("pyDrone não encontrado")
        return

    print("Conectando...")

    async with BleakClient(drone.address) as client:

        print("Conectado!")

        while True:

            roll = 127
            pitch = 127
            yaw = 127
            throttle = 127
            button = 0
            
            # Decolar
            if keyboard.is_pressed("space"):
                button = 24

            # Frente / trás
            if keyboard.is_pressed("w"):
                pitch = 255

            elif keyboard.is_pressed("s"):
                pitch = 0

            # Esquerda / direita
            if keyboard.is_pressed("a"):
                roll = 0

            elif keyboard.is_pressed("d"):
                roll = 255

            # Rotação
            if keyboard.is_pressed("q"):
                yaw = 0

            elif keyboard.is_pressed("e"):
                yaw = 255

            # Altitude
            if keyboard.is_pressed("r"):
                throttle = 255

            elif keyboard.is_pressed("f"):
                throttle = 0

            # Pousar
            if keyboard.is_pressed("enter"):
                button = 72

            # Emergência
            if keyboard.is_pressed("x"):
                button = 136

            await client.write_gatt_char(
                RX_UUID,
                pacote(
                    roll,
                    pitch,
                    yaw,
                    throttle,
                    button
                )
            )

            await asyncio.sleep(0.05)

asyncio.run(main())