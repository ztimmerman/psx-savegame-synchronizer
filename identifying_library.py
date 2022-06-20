import os

#Param(s):
#   file_data: binary info from the file as a single continuous 'bytes'.
#Returns 'PSP' if identified as PSP, 'single' if identified as a single save file,
#  and 'memCard' if identified as a PS1 memory card save
def f_identifyFile(file_data):
    file_type = None    #returned file data type
    MC_MAGIC = b'MC' #magic data that starts a PS1 memory card
    SC_MAGIC = b'SC' #magic data that starts a PS1 save file
    PMV_MAGIC = b'PMV' #magic data that starts a PSP save file
    PS1_STANDARD_MC_LEN = 128*1024 #Standard PS1 memory card is 128 KB long
    PSP_MC_LEN = 129*1024   #Length of the PSP memory card files

    #Basis of PSX MC detection
    if len(file_data) == PS1_STANDARD_MC_LEN:
        #PS1 memory cards have to start with "MC"
        if file_data[0x0:0x2] == MC_MAGIC:
            file_type = 'memCard'

    #Basis of PSP MC detection
    elif len(file_data) == PSP_MC_LEN:
        #PSP memcard saves have to start with "VMP"
        if file_data[0x0:0x0C] == "PMV":
            file_type = 'PSP'
    #Assume single save detection
    else:
        #Single saves have to start with the 'SC' magic data
        if file_data[0x0:0x2] == SC_MAGIC:
            file_type = 'single'

    return file_type

def tester():
    #Replace game save file paths as necessary.
    RETROARCH_MC_PATH = "Ace_Combat_3_Nemo.srm"
    retroarch_mc_data = open(RETROARCH_MC_PATH,'rb').read()
    PSX_SINGLE_SAVE_PATH = "BISLPSP02020AC3ES_MC"
    psx_single_save_data = open(PSX_SINGLE_SAVE_PATH,'rb').read()
    #print(len(retroarch_mc_data)/1024)

    #Test identifying file with data from each type of savegame.
    retroarch_mc_file_type = f_identifyFile(retroarch_mc_data)
    if retroarch_mc_file_type != 'memCard':
        raise Exception('file type should be memCard, not {}'.format(retroarch_mc_file_type))
    psx_single_save_file_type = f_identifyFile(psx_single_save_data)
    if psx_single_save_file_type != 'single':
        raise Exception('file type should be single, not {}'.format(psx_single_save_file_type))

if __name__ == '__main__':
    tester()