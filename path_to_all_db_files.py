import glob

########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
# --------------------------------------->>> PULL ALL CVS FILES FROM SKI DB <<<--------------------------------------- #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################

# path to DB
path = '/Users/pik/Desktop/SKI_DB'

# list of paths to all files in the SKI_DB
files_name = glob.glob(path + '/**/*.csv', recursive=True)

# target only individual tournaments
csv_files_list = [file for file in files_name if file.split('/')[7] == 'Individual']
