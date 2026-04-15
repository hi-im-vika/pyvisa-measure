import pyvisa

def main():
    print("Hello from pyvisa-measure!")
    rm = pyvisa.ResourceManager()
    print(rm.list_resources())

if __name__ == "__main__":
    main()