from sys import version as sys_version

version       = int(sys_version[:1])
version_major = sys_version[:1]
version_minor = sys_version[2:3]
version_full  = sys_version[:3]

def input(prompt):
    if version == 3:
        return input(prompt)
    else:
        return raw_input(prompt)
