'''
В этом паттерне есть четыре термина, пока примем их как данность: команды(command), приемник команд(receiver), вызывающий команды(invoker) и клиент(client).

есть класс Light, который умеет две вещи: включить свет и выключить. Он в терминах паттерна будет "приемник команд (receiver)"

Создадим интерфейс с одним методом execute(), который будет выполнять и который называется в терминах паттерна "команда (command)"

Класс Switch в терминах паттерна называется вызывающий команды (invoker). Пусть он будет принимать в конструкторе переменные Command

Умный дом строится на этом паттерне
'''
from abc import ABC, abstractmethod


class Light:

    def turn_on(self):
        print("light is on")

    def turn_off(self):
        print("light is off")


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class TurnOnLight(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffLight(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class Switch:

    def __init__(self, on_command: TurnOnLight, off_command: TurnOffLight):
        self.on_command = on_command
        self.off_command = off_command

    def press_up(self):
        self.on_command.execute()

    def press_down(self):
        self.off_command.execute()


if __name__ == '__main__':
    switch = Switch(TurnOnLight(Light()), TurnOffLight(Light()))

    switch.press_up()
    switch.press_down()

