#!/usr/bin/env python3

import pifacecad

if __name__ == "__main__":
  cad = pifacecad.PiFaceCAD()
  lcd = cad.lcd
  lcd.clear()
  lcd.display_off()
  lcd.backlight_off()
  lcd.cursor_off()
