import numpy as np
import random
from PIL import Image
from midiutil.MidiFile import MIDIFile

def main():
    mf = MIDIFile(1)
    track = 0
    time = 0
    mf.addTrackName(track,time,"Sample")
    mf.addTempo(track,time,160)

    channel = 0
    volume = 100
    pix = []
    for i in range(50):
        x = []
        for q in range(50):
            r1 = random.randint(0,255)
            r2 = random.randint(0,255)
            r3 = random.randint(0,255)
            x.append((r1,r2,r3))
            p1 = rgb_to_midi(r1)
            p2 = rgb_to_midi(r2)
            p3 = rgb_to_midi(r3)
            time = q
            print time
            duration = 1
            mf.addNote(track, channel, p1, q, duration, volume)
        pix.append(x)
    array = np.array(pix,dtype=np.uint8)
    new = Image.fromarray(array)
    new.save('new.png')
    with open("output.mid", 'wb') as outf:
        mf.writeFile(outf)

def rgb_to_midi(rgb):
    return 21 + (rgb%87)

def pixels_to_midi():
    pix = get_image_data("green.jpg")
    mf = MIDIFile(1)
    track = 0
    time = 0
    mf.addTrackName(track,time,"Sample")
    mf.addTempo(track,time,500)

    channel = 0
    volume = 100
    time = 0
    for i in pix:
        p1 = rgb_to_midi(i[0])
        p2 = rgb_to_midi(i[1])
        p3 = rgb_to_midi(i[2])
        duration = 1
        if time % 4 == 0:
            mf.addNote(track, channel, p1, time, 4, volume)
            mf.addNote(track, channel, p2, time, 4, volume)
            mf.addNote(track, channel, p3, time, 4, volume)
        else:
            mf.addNote(track, channel, p1, time, duration, volume)
        time += 1
    with open("green.mid", 'wb') as outf:
        mf.writeFile(outf)

def pixels_to_midi2():
    pix = get_image_data("green.jpg")
    mf = MIDIFile(1)
    track = 0
    time = 0
    mf.addTrackName(track,time,"Sample")
    mf.addTempo(track,time,1000)

    channel = 0
    volume = 100
    time = 0
    for i in xrange(len(pix)):
        if i >= len(pix)-4:
            break
        p1 = rgb_to_midi(pix[i])
        p2 = rgb_to_midi(pix[i+1])
        p3 = rgb_to_midi(pix[i+2])
        duration = 1
        if time % 4 == 0:
            mf.addNote(track, channel, p1, time, 4, volume)
            mf.addNote(track, channel, p2, time, 4, volume)
            mf.addNote(track, channel, p3, time, 4, volume)
        else:
            mf.addNote(track, channel, p1, time, duration, volume)
        time += 1
    with open("green.mid", 'wb') as outf:
        mf.writeFile(outf)

def get_image_data(img):
    im = Image.open(img)
    pix = list(im.getdata())
    return pix

def p():
    pix = []
    for i in range(10):
        x = []
        x.append((0,50,250))
        x.append((1,50,250))
        x.append((2,50,250))
        x.append((3,50,250))
        x.append((4,50,250))

        x.append((5,50,20))
        x.append((6,50,20))
        x.append((7,50,20))
        x.append((8,50,20))
        x.append((9,50,20))

        pix.append(x)

    array = np.array(pix,dtype=np.uint8)
    new = Image.fromarray(array)
    new.save('p.png')

def midi():
    mf = MIDIFile(1)
    track = 0
    time = 0
    mf.addTrackName(track,time,"Sample")
    mf.addTempo(track,time,120)

    channel = 0
    volume = 100

    pitch = 60           # C4 (middle C)
    time = 0             # start on beat 0
    duration = 1         # 1 beat long
    mf.addNote(track, channel, pitch, time, duration, volume)

    # write it to disk
    with open("output.mid", 'wb') as outf:
        mf.writeFile(outf)

if __name__ == "__main__": main()
