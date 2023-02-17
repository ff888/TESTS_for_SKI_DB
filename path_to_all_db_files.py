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
csv_files_list = glob.glob(path + '/**/*.csv', recursive=True)

# csv_files_list = ['/Users/pik/Desktop/SKI_DB/Man/World Cup/Individual/2018-2019/2019-02-02_Oberstdorf(GER)_(5255)_WC_SF_M_I.csv',
# '/Users/pik/Desktop/SKI_DB/Man/World Cup/Individual/2018-2019/2018-12-15_Engelberg(SUI)_(5237)_WC_LH_M_I.csv']
