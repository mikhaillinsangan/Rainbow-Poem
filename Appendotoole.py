def Appendotoole(SetNames, NewSetItems, IARList, OARList, otooleOutputDirectory, OsemosysGlobalPath):
    import os
    import shutil
    if not os.path.exists(otooleOutputDirectory):
        os.makedirs(otooleOutputDirectory)

    # Ouptut the sets for otoole:
    for SetName in SetNames:
        with open(os.path.join(otooleOutputDirectory, SetName + '.csv'),'w') as f:
            with open(os.path.join(OsemosysGlobalPath, SetName + '.csv'), 'r') as fin:
                if SetName == 'MODE_OF_OPERATION':
                    for items in NewSetItems[SetNames.index(SetName)]:
                        f.write(items['value']+'\n')
                else:
                    f.write(fin.read())
                    for items in NewSetItems[SetNames.index(SetName)]:
                        f.write(items['value']+'\n')
    
    # And output the IAR for otoole:
    #appnd IARList items to otoole output file
    with open(os.path.join(otooleOutputDirectory, 'InputActivityRatio.csv'),'w') as f:
        with open(os.path.join(OsemosysGlobalPath, 'InputActivityRatio.csv'), 'r') as fin:
            f.write(fin.read())
            for item in IARList:
                f.write(str(item['c'][0])+','+str(item['c'][1])+','+str(item['c'][2])+','+str(item['c'][3])+','+str(item['c'][4])+','+str(item['v'])+'\n')

    # And output the OAR for otoole:
    with open(os.path.join(otooleOutputDirectory, 'OutputActivityRatio.csv'),'w') as f:
        with open(os.path.join(OsemosysGlobalPath, 'OutputActivityRatio.csv'), 'r') as fin:
            f.write(fin.read())
            for item in OARList:
                f.write(str(item['c'][0])+','+str(item['c'][1])+','+str(item['c'][2])+','+str(item['c'][3])+','+str(item['c'][4])+','+str(item['v'])+'\n')
                
    for file in os.listdir(OsemosysGlobalPath):
        if not os.path.exists(os.path.join(otooleOutputDirectory, file)):
            shutil.copyfile(os.path.join(OsemosysGlobalPath, file), os.path.join(otooleOutputDirectory, file))
            
    os.rename(otooleOutputDirectory + 'COMMODITY.csv', otooleOutputDirectory + 'FUEL.csv')
#   os.remove(otooleOutputDirectory + 'MODE_OF_OPERATION.csv')
#   shutil.copyfile(OsemosysGlobalPath + 'MODE_OF_OPERATION.csv', otooleOutputDirectory + 'MODE_OF_OPERATION.csv')
