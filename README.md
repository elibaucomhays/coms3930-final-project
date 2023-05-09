# coms3930-final-project

<p align="center">
  <img width="300" height="400" src="/finalprojectdemo.png">
</p>

This readMe keeps it short with just the key information on usage. To read more, check out my [blog](https://www.notion.so/Final-Project-2d60b81b1ed6494ebbba6a5292fcaf32?pvs=4)!

<br />

**Necessary hardware for this project:**
<br />
- ESP32 TTGO T-Display
- A USB-C cable to connect to the ESP32
- A computer that can connect to your USB-C cable 
- A breadboard
- A joystick that can connect to the breadboard
- A button that can connect to the breadboar
- - wires to connect components on the breadboard

<br />

**Necessary software for this project:**
<br />
- Arduino
- Python (I used Pycharm IDE)
- Sonic Pi

<br />

**To use Arduino:**
<br />
1. Follow [this link](https://www.arduino.cc/en/software) to download it Arduino if you need to.
2. Make sure you have configured your Arduino environment to use your ESP32. Open the Arduino IDE and go to \<File\>, \<Preferences\>, and paste this [link](https://dl.espressif.com/dl/package_esp32_index.json) into the “Additional Boards Manager URLs” field and hit OK. Then, go to \<Tools\>, \<Manage Libraries\>, and install “tft_eSPI” by “Bodmer”. Then go to \<Tools\>, \<Board\>, \<ESP32 Arduino\>, and then select the “TTGO T1” option. Then go to where your libraries are stored on your computer, and look for the “TFT_eSPI” folder, and open up the User_Setup_Select.h file. Comment out the line “#include <User_Setup.h>” and uncomment the line “#include <User_Setups/Setup25_TTGO_T_Display.h>”
3. Download the file from here called final_project_sketch.ino and open it in the Arduino IDE. With your ESP32 plugged in, hit the upload button (it looks like an arrow pointing to the right).

**To use the Python script:**
If you just want to run the script here called pick_up_signals.py, you likely will be able to do so if you have Python installed on your computer (which most computers these days do). However, the fun comes from experimenting, so if you do not have a Python IDE that you can manipulate the code with, I recommend installing Pycharm (you can find the link and instructions [here](https://www.jetbrains.com/pycharm/download/#section=windows)). 

**To use Sonic Pi:**
If you do not already have Sonic Pi downloaded, you can get it [here](https://sonic-pi.net/). For help experimenting with writing your own code, [here](https://sonic-pi.net/tutorial.html) is a tutorial on how to use Sonic Pi. Specifically check out the explanations linked to learn more about [live coding](https://sonic-pi.net/tutorial.html#section-9) and sending/receiving [OSC messages](https://sonic-pi.net/tutorial.html#section-12). 

**Make sure to:**
- Upload the Arduino code to your ESP32 first, then run the Python program, and then run the Sonic Pi program so that when you run the Sonic Pi program, the Arduino Program and Python programs are already also running. 
- Make sure not to have the serial monitor open in Arduino when you try to run one of the other programs. 
- If it is not working right away, double check that you started running each program in the order mentioned above. Try pressing the button and/or joystick a couple times to check that it is working. 
