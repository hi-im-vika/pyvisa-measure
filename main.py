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
    vm.write('APPL CH1, 12V, 1A')
    vm.write('OUTP ON')
    print('Power on... waiting for settling')
    # need a little delay right here
    time.sleep(3)
    print('Taking measurements')
    voltCH1 = float(vm.query('MEAS:VOLT? CH1'))
    currentCH1 = float(vm.query('MEAS:CURR? CH1'))
    powerCH1 = voltCH1 * currentCH1
    print(f'V={voltCH1:.1f}V I={currentCH1:.2f}A P={powerCH1:.2f}W')
    vm.write('OUTP OFF')
    print('Turned off power')

if __name__ == "__main__":
    main()