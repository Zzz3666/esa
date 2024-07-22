import streamlit as st
import numpy as np
import pandas as pd

dac_bit = st.slider('Select a DAC bit', 1, 32, 16, 1)
dac_max_value = 2 ** dac_bit - 1
normal_work_value = round(dac_max_value / 1.2)
protect_value = round(normal_work_value * 1.1)
protect_value_sin = round(normal_work_value * 1.15)
sin_max_amplitude = st.slider('Select a sin max amplitude', 0.0, 1.0, 0.2, 0.1)
st.write('DAC max value', dac_max_value)
st.write('Normal work value', normal_work_value)
st.write('Protect value', protect_value )
st.write('Protect value sin', protect_value_sin )

sin_frequency = st.slider('Select a sin rfrequency[Hz]', 1, 10, 5, 1)
base_frequency = st.slider('Select a base frequency[kHz]', 1, 10, 1, 1)

x = np.linspace(0, 2 * np.pi * sin_frequency, base_frequency * 1000)
line_work_line = np.linspace(normal_work_value, 
                             normal_work_value, base_frequency * 1000)
line_sin_max = np.linspace(normal_work_value * (1 + sin_max_amplitude / 2), 
                           normal_work_value * (1 + sin_max_amplitude / 2), 
                           base_frequency * 1000)
line_sin_min = np.linspace(normal_work_value * (1 - sin_max_amplitude / 2), 
                           normal_work_value * (1 - sin_max_amplitude / 2),
                           base_frequency * 1000)
normal_work_protect_line = np.linspace(protect_value, 
                                       protect_value, 
                                       base_frequency * 1000)
wave_work_protect_line = np.linspace(protect_value_sin, 
                                       protect_value_sin, 
                                       base_frequency * 1000)
y = np.sin(x) * normal_work_value * (sin_max_amplitude/2) + normal_work_value
chart_data = pd.DataFrame({'Wave Work':y,
                           'Normal Work':line_work_line, 
                           'Sin Max':line_sin_max, 
                           'Sin Min':line_sin_min,
                           'Normal work protect value':normal_work_protect_line,
                           'Wave work protect value':wave_work_protect_line})
st.line_chart(chart_data)