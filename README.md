# ZCR
Zero Crossing Rate (ZCR) in a Sine Wave
The Zero Crossing Rate (ZCR) measures how many times a signal crosses the zero axis within a given time interval. In other words, it counts how frequently the amplitude of the signal changes its sign (from positive to negative or vice versa).
ZCR is calculated by:

![image](https://github.com/user-attachments/assets/67ed8c20-c14a-4d54-825a-15d679027579)

where, s(n) — Signal value at time and N — Length of the signal

## 1. ZCR.py

In the code, initially do signal generation:
* Signal Generation:
    fs = 1000 — Sampling frequency (samples per second);  
    f = 5 — Frequency of the sine wave (5 Hz);  
    duration = 1 sec — 5 cycles of sine wave in 1 second
* Then Zero Crossing Detection:
    np.diff(np.sign(sine_wave)) — Computes the difference of sign changes; np.where() — Identifies indices where zero crossings occur.

* ZCR Calculation:
    𝑍𝐶𝑅=Number of zero crossings/duration
  

  
### Output
​Zero Crossing Rate (ZCR): 10.00 crossings per second

![image](https://github.com/user-attachments/assets/384f3352-85d7-4458-a9e7-a9686f2a41b4)

## 2. ZCR_speech.py
To calculate the total number of zero crossings and zero crossing rate in the following audio file: (the sample audio is available in the same folder) 
![image](https://github.com/user-attachments/assets/1eaed77b-0e44-48a9-b0ca-71002e6208cd)
* Total Zero Crossing: 307
* Average Zero Crossing Rate: 0.1407 crossings per frame
![image](https://github.com/user-attachments/assets/7a26ff29-bf2a-40b8-bfcb-af8ecf96a337)


## Use Case:
* Speech Processing: To detect voiced/unvoiced segments.
* Music Analysis: To differentiate between percussive and tonal components.
* Audio Classification: For identifying different types of sounds.
## Prerequesits 
matplotlib and numpy
