import machine

voltage_sensor_pin = machine.Pin(26)
voltage_sensor = machine.ADC(voltage_sensor_pin)


def get_voltage():
    R1 = 30000.0
    R2 = 7500.0
    VRef = 3.33
    
    adc_value = voltage_sensor.read_u16()
    adc_voltage  = (adc_value * VRef) / 65535.0
    battery_voltage = adc_voltage*(R1+R2)/R2
    return battery_voltage
            

def get_battery():
    avg_sum = 0
    for i in range(5):
        avg_sum += get_voltage()

    avg_voltage = avg_sum/5

    battery_percentage = round(((avg_voltage - 3.7) / (4.2 - 3.7) * 100))

    return battery_percentage

    