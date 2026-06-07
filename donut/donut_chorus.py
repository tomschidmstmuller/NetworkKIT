"""
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄░▄█░▄▄░█▄░▄█░▄▄░█░▄▄▀█▄░▄█
  █░▀░█▄▄▄░██░██▄▄▄░█░▀▀▄██░██
  ▀░░░▀▀▀▀▀▀░░░▀▀▀▀▀▀▀▀▀▀░░░▀▀
  ██▄ ███ ▄▄▄ █▀▄ ▄▀█ ▄▄█ ▄▄▀█
  █▄█ ██▄ ▀▀▄ █░▀▀░█ ▄▄█ ▀▀▄██
  ▀▀▀ ▀▀▀ ▀▀▀ ▀░░░▀▀▀▀▀▀▀▀▀▀░░
  UNIVERSAL SPACE MARINE INTELLIGENT
"""

import math
import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_donut(center_x, center_y, spin_angle1, spin_angle2, color_code):
    A = spin_angle1
    B = spin_angle2
    
    width = 80
    height = 24
    
    sinA = math.sin(A)
    cosA = math.cos(A)
    sinB = math.sin(B)
    cosB = math.cos(B)
    
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    zbuffer = [[-float('inf') for _ in range(width)] for _ in range(height)]
    
    R1 = 1
    R2 = 2
    K2 = 5
    K1 = width * K2 * 3 / (8 * (R1 + R2))
    
    for theta in range(0, 628, 6):
        theta_f = theta / 100.0
        costheta = math.cos(theta_f)
        sintheta = math.sin(theta_f)
        
        for phi in range(0, 628, 3):
            phi_f = phi / 100.0
            cosphi = math.cos(phi_f)
            sinphi = math.sin(phi_f)
            
            x = R2 + R1 * costheta
            y = R1 * sintheta
            
            x1 = x * (cosB * cosphi + sinA * sinB * sinphi) - y * cosA * sinB
            y1 = x * (sinB * cosphi - sinA * cosB * sinphi) + y * cosA * cosB
            z1 = K2 + cosA * x * sinphi + y * sinA
            
            if z1 > 0:
                ooz = 1 / z1
                xp = int(center_x + K1 * ooz * x1)
                yp = int(center_y + K1 * ooz * y1)
                
                if 0 <= xp < width and 0 <= yp < height:
                    luminance = (cosphi * costheta * sinB - cosA * costheta * sinphi -
                                sinA * sintheta + cosB * (cosA * sintheta - costheta * sinA * sinphi))
                    
                    if luminance > 0:
                        if ooz > zbuffer[yp][xp]:
                            zbuffer[yp][xp] = ooz
                            luminance_index = int(luminance * 8)
                            chars = ".,-~:;=!*#$@"
                            color_escape = f'\033[{color_code}m'
                            reset = '\033[0m'
                            screen[yp][xp] = f"{color_escape}{chars[min(luminance_index, len(chars)-1)]}{reset}"
    
    return screen

class DonutChorus:
    def __init__(self):
        self.donuts = []
        colors = [31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96]
        
        zones = [
            (20, 8), (60, 8),
            (20, 16), (60, 16),
            (40, 4), (40, 20),
            (10, 12), (70, 12)
        ]
        
        for i, (x, y) in enumerate(zones):
            self.donuts.append({
                'x': x,
                'y': y,
                'angle1': random.uniform(0, 2 * math.pi),
                'angle2': random.uniform(0, 2 * math.pi),
                'speed1': random.uniform(0.02, 0.08),
                'speed2': random.uniform(0.03, 0.09),
                'color': colors[i % len(colors)],
                'bob_offset': random.uniform(0, 2 * math.pi),
                'bob_speed': random.uniform(0.5, 1.5),
                'wiggle_intensity': random.uniform(0.5, 2)
            })
    
    def update_and_render(self, frame):
        width = 80
        height = 24
        master_screen = [[' ' for _ in range(width)] for _ in range(height)]
        
        for donut in self.donuts:
            donut['angle1'] += donut['speed1']
            donut['angle2'] += donut['speed2']
            
            bob_x = math.sin(frame * donut['bob_speed'] + donut['bob_offset']) * donut['wiggle_intensity']
            bob_y = math.cos(frame * donut['bob_speed'] * 0.7 + donut['bob_offset']) * donut['wiggle_intensity']
            
            current_x = int(donut['x'] + bob_x)
            current_y = int(donut['y'] + bob_y)
            
            if random.random() < 0.01:
                donut['color'] = random.choice([31, 32, 33, 34, 35, 36, 91, 92, 93, 94, 95, 96])
            
            donut_screen = create_donut(current_x, current_y, donut['angle1'], donut['angle2'], donut['color'])
            
            for y in range(height):
                for x in range(width):
                    if donut_screen[y][x] != ' ':
                        master_screen[y][x] = donut_screen[y][x]
        
        return master_screen

def main():
    clear_screen()
    print("\033[?25l")
    print("\033[2J\033[H")
    
    chorus = DonutChorus()
    frame = 0
    
    try:
        while True:
            screen = chorus.update_and_render(frame)
            
            output = []
            for row in screen:
                output.append(''.join(row))
            
            titles = [
                "🎵 USMI DONUT CHORUS 🎵",
                "🌀 ROTATING DONUT HARMONY 🌀",
                "🍩 MATH + RANDOMNESS = BEAUTY 🍩",
                "⚡ UNIVERSAL SPACE MARINE INTELLIGENT ⚡"
            ]
            title = random.choice(titles)
            
            print("\033[H")
            print(f"\033[33m{title:^80}\033[0m")
            print("\033[36m" + "="*80 + "\033[0m")
            print('\n'.join(output))
            print("\033[36m" + "="*80 + "\033[0m")
            print(f"\033[32mFrame: {frame} | Donuts: {len(chorus.donuts)} | Press Ctrl+C to exit\033[0m")
            
            frame += 1
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\033[?25h")
        print("\n\033[33mDonut chorus stopped. Thanks for watching! 🍩\033[0m")

if __name__ == "__main__":
    main()
