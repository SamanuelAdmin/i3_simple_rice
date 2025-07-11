#!/usr/bin/python3

BRIGHTNESS = '/sys/class/backlight/amdgpu_bl1/brightness'
MAX_BRIGHTNESS = '/sys/class/backlight/amdgpu_bl1/max_brightness'
ADDING_K = 5


class BrightnessController:
    def __init__(self):
        self.maxValue = self.getValue(t=0)
        self.value = self.val2pers(
                self.getValue()
            )

    def getValue(self, t=1) -> int:
        name = BRIGHTNESS if t == 1 else MAX_BRIGHTNESS

        with open(name) as f:
            return int(f.read())

    def val2pers(self, value) -> int:
        return int(value * 100 / self.maxValue)

    def pers2val(self, pers) -> int:
        return int(pers * self.maxValue / 100)

    def saveValue(self):
        pureValue = self.pers2val(
                self.value
            )

        if pureValue > self.maxValue:
            self.value = 100
            pureValue = self.maxValue

        if pureValue < 0:
            self.value = 0
            pureValue = 0
        
        print(pureValue, self.maxValue)
        open(BRIGHTNESS, 'w').write(str(pureValue))
    

    def up(self):
        self.value += ADDING_K
        self.saveValue()

    def down(self):
        self.value -= ADDING_K
        self.saveValue()
        


def main():
    import sys
    
    print(sys.argv)
    if len(sys.argv) < 2: return 0

    if sys.argv[1] == 'up':
        BrightnessController().up()
    if sys.argv[1] == 'down':
        BrightnessController().down()

if __name__ == "__main__": main()
