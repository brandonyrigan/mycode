#!/usr/bin/env python3

# import library
import shutil
import os

def main():
    # force program to start in home user directory
    os.chdir('/home/student/mycode/')

    # move file to destination
    shutil.move('raynor.obj', 'ceph_storage/')

    # get user input for new file name
    xname = input('What is the new name for kerrigan.obj? ')
    # change file name with user input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
