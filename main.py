import pyvisa
import time

def main():
    print("Hello from pyvisa-measure!")

    # check if pyvisa is working
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    print(resources)

    # demo code from https://iotexpert.com/pyvisa-first-use/
    vm = rm.open_resource(resources[0])

    # Turn on remote mode (so that SCPI commands work)
    vm.write('SYST:REM')
    vm.write('APPL CH1, 3.7V, 4A')  # simulate 18650 battery
    vm.write('OUTP ON')
    print('Power on... waiting for settling')
    # need a little delay right here
    time.sleep(3)
    print('Taking measurements')
    try:
        while True:
            voltCH1 = float(vm.query('MEAS:VOLT? CH1'))
            currentCH1 = float(vm.query('MEAS:CURR? CH1'))
            powerCH1 = voltCH1 * currentCH1
            print(f'V={voltCH1:.1f}V I={currentCH1:.2f}A P={powerCH1:.2f}W')
            # time.sleep(1)
    except:
        pass
    vm.write('OUTP OFF')
    print('Turned off power')

if __name__ == "__main__":
    main()