import requests

def format_voltage(value):
    volts = float(value) / 1000

    if volts >= 10:
        return f"{volts:.1f}V"

    return f"{volts:.2f}V"


r = requests.get('http://192.168.1.3/api/system/info')
print(f"[+] AxeOS Power Stats [-]")

#power
#input voltage
#asic freq
#asic voltage

json_data = r.json()

print(f"Power: {int(json_data.get('power'))}w")
print(f"Input Voltage: {format_voltage(json_data.get('voltage'))}")
print(f"Current: {int(json_data.get('current'))/1000}A")
print(f"ASIC Frequency: {json_data.get('actualFrequency')}MHz")
print(f"ASIC Voltage: {format_voltage(json_data.get('coreVoltageActual'))}")
