import os.path
import os


def show_contents():
    for fn in os.listdir('.'):
        if os.path.isfile(fn):
            print (fn)


def sort():
    for file in os.listdir('.'):
        if os.path.isfile(file):
            print ("File: " + str(file))
            print file[0:4]
            # print ("Oldfile: " +str(oldfile))
            if file[0:4] == "buck":
                print("MOVING")
                print "/Users/ash/PycharmProjects/deerApp/" + file
                os.rename("/Users/ash/PycharmProjects/deerApp/" + file,
                          "/Users/ash/PycharmProjects/deerApp/bucks/" + file)


def main():
    sort()


main()
