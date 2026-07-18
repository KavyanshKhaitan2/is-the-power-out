# Is the power out?
<center><a href="https://macondo.hackclub.com/projects/13857">Find this project on Macondo</a></center>

A project that when plugged into the outlet, logs when there is a power cut and when the power is back, and sends it in a Slack channel using a webhook URL!

In my town, we frequently lose power, so I can use this to know exactly when, and for how long the power is gone!

## Wiring Diagram / Schematic
<img width="962" height="833" alt="image" src="https://github.com/user-attachments/assets/6976fb57-e296-44fa-b583-112872b951e3" />

[ [View in KiCanvas](https://kicanvas.org/?repo=https%3A%2F%2Fgithub.com%2FKavyanshKhaitan2%2Fis-the-power-out) ]

## 3D models
<img width="827" height="720" alt="image" src="https://github.com/user-attachments/assets/7ffd025a-2bc7-4231-8689-6d1e952648cc" />

[ [View in OnShape](https://cad.onshape.com/documents/09c2e1066698d982f6b4db91/w/a2dfad63af4ed4408f592306/e/a1a8967d97607ce5d6740ca7?renderMode=0&uiState=6a5b6723fb9e1354944692a0) ]

- [Download main case part](https://github.com/KavyanshKhaitan2/is-the-power-out/blob/main/3dp/Case%20-%20Part%201.stl) (PLEASE print with supports!)
- [Download case top](https://github.com/KavyanshKhaitan2/is-the-power-out/blob/main/3dp/Case%20-%20Part%202.stl)

## BOM
- [ [View BOM on Google Sheets](https://docs.google.com/spreadsheets/d/1HpNvNYVS15Ou1rxpnCsINuQ82Mtfe6AI-b8NtTX2ELQ/edit?usp=sharing) ]
- [ [View BOM in GitHub](https://github.com/KavyanshKhaitan2/is-the-power-out/blob/main/bom.csv) ]

## Code
- Flash the Pi Pico with MicroPython
- Copy the `main.py` file in this repo over to the Pico
- Change the SSID and Password on the `main.py` file
- Change the webhook URL in the `main.py` file
