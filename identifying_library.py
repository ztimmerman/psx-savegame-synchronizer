#Param(s):
#   file_data: binary info from the file as a single continuous 'bytes'.
#Returns 'PSP' if identified as PSP, 'single' if identified as a single save file,
#  and 'memCard' if identified as a PS1 memory card save
def f_identifyFile(file_data):
    MC_MAGIC = b'MC' #magic bit that starts a PS1 memory card
    SC_MAGIC = b'SC'
    PS1_STANDARD_MC_LEN = 128*1024 #Standard PS1 memory card is 128 KB long
    PSP_MC_LEN = 129*1024   #Length of the PSP memory card files