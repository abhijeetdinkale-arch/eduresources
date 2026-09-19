import os
import subprocess

print("Fixing PHY175 Revision Book & compiling...")

# Fix Unit 6 Revision
u6_rev = r"""\chapter{Arduino and Sensors: Rapid Revision}

\begin{highyieldbox}[Embedded System \& Sensor Summary]
\begin{itemize}[leftmargin=*]
    \item \textbf{Analog vs Digital:} Continuous vs discrete voltage levels. Nyquist rate: $f_s \ge 2 f_{max}$.
    \item \textbf{Arduino Uno 10-Bit ADC:} Quantization levels $= 1024$. Resolution $= \frac{5.0\,\text{V}}{1024} = 4.88\,\text{mV/LSB}$.
    \item \textbf{PWM Output:} Timer-based square wave on pins 3, 5, 6, 9, 10, 11. Average voltage $V_{avg} = \frac{\text{duty}}{255} \times 5.0\,\text{V}$.
    \item \textbf{Hardware Buses on Uno:} UART (D0, D1), I2C (A4=SDA, A5=SCL), SPI (D10=SS, D11=MOSI, D12=MISO, D13=SCK).
    \item \textbf{IR Sensor:} IR LED + Photodiode receiver + LM393 comparator. Detects obstacles via reflected infrared; sensitive to sunlight and dark surfaces.
    \item \textbf{LDR Photoresistor:} CdS sensor. Light increases $\implies$ resistance drops from $\text{M}\Omega$ to $\text{k}\Omega \implies$ voltage divider output rises. Hysteresis prevents streetlight flickering.
    \item \textbf{Ultrasonic HC-SR04:} Emits $40\,\text{kHz}$ burst. Distance formula $d = \frac{v_{sound} \cdot t_{echo}}{2} = \frac{(340\,\text{m/s}) \cdot t_{echo}}{2}$.
    \item \textbf{DHT11 vs DHT22:} DHT11 ($0-50^\circ\text{C}, 1\,\text{Hz}$ rate); DHT22 ($-40-80^\circ\text{C}, 0.5\,\text{Hz}$ rate, higher accuracy). Both use a single-wire digital bus with pull-up.
\end{itemize}
\end{highyieldbox}
"""

with open("PHY175_Revision_Book/chapters/unit6-revision.tex", "w") as f:
    f.write(u6_rev)

print("Updated unit6-revision.tex")
