import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000


try:                                                                                                                                                                                                                                           
    dac = mcp.MCP4725(5, 0x61, False)

    start_time = time.time()

    while True:
        work_time = time.time() - start_time

        voltage = (sg.get_sin_wave_amplitude(signal_frequency, work_time)) * amplitude
        dac.set_voltage(voltage)

        sg.wait_for_sampling_period(sampling_frequency)


finally:
    dac.deinit()
