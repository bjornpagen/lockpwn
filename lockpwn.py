#!/bin/env python3

import argparse, textwrap
import math
import sys

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
            lockpwn
            ----------------------------------------------------------
                Adapted from https://samy.pl/master/master.html
        '''),
        epilog=textwrap.dedent('''
            Walkthrough:
            ----------------------------------------------------------
                1. Set the dial to 0.
                
                2. Apply full pressure upward on the shackle as if trying to
                open it.
                
                3. Rotate dial to the left (towards 10) hard until the dial
                gets locked.
                
                4. Notice how the dial is locked into a small groove. If you're
                directly between two digits such as 3 and 4, release the
                shackle and turn the dial left further until you're into the
                next locked groove. However, if the dial is between two half
                digits (eg 2.5 and 3.5), then enter the digit in-between into
                First Locked Position (eg, 3).
                
                5. Do this again until you find the second digit below 11 that
                is between two half digits (eg 5.5 and 6.5), and enter the
                whole number in Second Locked Position (eg, 7).
                
                6. Apply half as much pressure to the shackle so that you can
                turn the dial.
                
                7. Rotate dial to the right until you feel resistance. Rotate
                the dial to the right several more times to ensure you're
                feeling resistance at the same exact location.
                
                8. Enter this number in Resistant Location. If the resistance
                begins at a half number, such as 14.5, enter 14.5.
                
                9. Click Find Combos!
            
            Why did I make this
            - bjornpagen@gmail.com
        ''')
    )

    parser.add_argument('l1', metavar='l1', type=int, help='first locked position: whole # under 11') 
    parser.add_argument('l2', metavar='l2', type=int, help='second locked position(s): whole # under 11') 
    parser.add_argument('rl', metavar='rl', type=float, help='resistant location(s): whole or half # (eg 4 or 4.5)')
    args = parser.parse_args()

    combo(args.l1, args.l2, args.rl)
    
def combo(l1, l2, rl):
    o1 = (math.ceil(rl + 5) % 40)
    o2 = []
    o3 = []

    print("""
    lockpwn
    ----------------------------------------------------------
         Adapted from https://samy.pl/master/master.html
         """)
    print("First number is: " + str(o1))

    mod = (o1 % 4)
    for i in range(10):
        tmp = ((mod + 2) % 4) + 4 * i
        o2.append(tmp)

    print("Second numbers could be: " + str(o2))

    for i in range(4):
        if ((10*i)+l1) % 4 == mod:
            o3.append(10*i + l1)
        if ((10*i)+l2) % 4 == mod:
            o3.append(10*i + l2)

    print("To narrow the results, choose the third digit: " + str(o3[:2]))

    for i in range(4):
        if i == 3:
            print("Giving up...")
            sys.exit(1)
        prompt = input()
        try: 
            pint = int(prompt)
            if pint != o3[0] and pint != o3[1]:
                print('Please enter either ' +
                    str(o3[0]) + ' or ' + str(o3[1]) + "...")
            else:
                frl = pint    
                break
        except:
            print('Please enter either ' +
                str(o3[0]) + ' or ' + str(o3[1]) + "...")
    
    print()
    print('--------------------< FINAL VALUES >--------------------')
    print()
    print("First number is: " + str(o1))

    fo2 = []
    for n in o2:
        if (frl+2)%40 != n and (frl-2)%40 !=n:
            fo2.append(n)

    print("Second numbers could be: " + str(fo2))
    print("Third number is: " + str(frl))
    
if __name__ == '__main__':
    main()
