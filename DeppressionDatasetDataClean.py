from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from tkinter import *

# Packages for analysis
import pandas as pd
import numpy as np

# Packages for visuals
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(font_scale=1.2)

def minMax(dataframe):

    condition_minmax1 = dataframe



    condition_temp1 = dataframe
    conditionOutput1 = dataframe[0:0]

    i = len(dataframe)

    counter = 60

    while counter < i:

        condition_temp1 = dataframe[counter - 60:counter]

        condition_minmax1['maxMinusMin'] = condition_temp1['activity'].max().astype(int) - condition_temp1['activity'].min().astype(int)

        conditionOutput1 = conditionOutput1.append(condition_minmax1[counter:counter + 1])

        counter += 60

    conditionOutput1['averageAll'] = dataframe['activity'].mean().astype(int)
    conditionOutput1['average'] = conditionOutput1['maxMinusMin'].mean().astype(int)
    conditionOutput1['median'] = conditionOutput1['maxMinusMin'].median().astype(int)

    conditionOutput1 = conditionOutput1[0:1]

    #print("dataframen etterpå: ", conditionOutput1)


   # conditionOutput1= conditionOutput1.astype(int)
   # pd.options.display.float_format = '{:,.0f}'.format
  #  df


    return conditionOutput1



condition_1 = pd.read_csv('condition_1.csv')

print('printer ut datasett 1 i sin reneste form: ')
print(condition_1)

condition_1 = condition_1
condition_1['maxMinusMin'] = ""
condition_1 = minMax(condition_1)
condition_1['control'] = '1'

print("printer det så ut etter datatransformeringen: ")
print(condition_1)

condition_2 = pd.read_csv('condition_2.csv')
condition_2 = condition_2
condition_2['maxMinusMin'] = ""
condition_2 = minMax(condition_2)
condition_2['control'] = '1'

condition_3 = pd.read_csv('condition_3.csv')
condition_3 = condition_3
condition_3['maxMinusMin'] = ""
condition_3 = minMax(condition_3)
condition_3['control'] = '1'

condition_4 = pd.read_csv('condition_4.csv')
condition_4 = condition_4
condition_4['maxMinusMin'] = ""
condition_4 = minMax(condition_4)
condition_4['control'] = '1'

condition_5 = pd.read_csv('condition_5.csv')
condition_5 = condition_5
condition_5['maxMinusMin'] = ""
condition_5 = minMax(condition_5)
condition_5['control'] = '1'

condition_6 = pd.read_csv('condition_6.csv')
condition_6 = condition_6
condition_6['maxMinusMin'] = ""
condition_6 = minMax(condition_6)
condition_6['control'] = '1'

condition_7 = pd.read_csv('condition_7.csv')
condition_7 = condition_7
condition_7['maxMinusMin'] = ""
condition_7 = minMax(condition_7)
condition_7['control'] = '1'

condition_8 = pd.read_csv('condition_8.csv')
condition_8 = condition_8
condition_8['maxMinusMin'] = ""
condition_8 = minMax(condition_8)
condition_8['control'] = '1'

condition_9 = pd.read_csv('condition_9.csv')
condition_9 = condition_9
condition_9['maxMinusMin'] = ""
condition_9 = minMax(condition_9)
condition_9['control'] = '1'

condition_10 = pd.read_csv('condition_10.csv')
condition_10 = condition_10
condition_10['maxMinusMin'] = ""
condition_10 = minMax(condition_10)
condition_10['control'] = '1'

condition_11 = pd.read_csv('condition_11.csv')
condition_11 = condition_11
condition_11['maxMinusMin'] = ""
condition_11 = minMax(condition_11)
condition_11['control'] = '1'

condition_12 = pd.read_csv('condition_12.csv')
condition_12 = condition_12
condition_12['maxMinusMin'] = ""
condition_12 = minMax(condition_12)
condition_12['control'] = '1'

condition_13 = pd.read_csv('condition_13.csv')
condition_13 = condition_13
condition_13['maxMinusMin'] = ""
condition_13 = minMax(condition_13)
condition_13['control'] = '1'

condition_14 = pd.read_csv('condition_14.csv')
condition_14 = condition_14
condition_14['maxMinusMin'] = ""
condition_14 = minMax(condition_14)
condition_14['control'] = '1'

condition_15 = pd.read_csv('condition_15.csv')
condition_15 = condition_15
condition_15['maxMinusMin'] = ""
condition_15 = minMax(condition_15)
condition_15['control'] = '1'

condition_16 = pd.read_csv('condition_16.csv')
condition_16 = condition_16
condition_16['maxMinusMin'] = ""
condition_16 = minMax(condition_16)
condition_16['control'] = '1'

condition_17 = pd.read_csv('condition_17.csv')
condition_17 = condition_17
condition_17['maxMinusMin'] = ""
condition_17 = minMax(condition_17)
condition_17['control'] = '1'

condition_18 = pd.read_csv('condition_18.csv')
condition_18 = condition_18
condition_18['maxMinusMin'] = ""
condition_18 = minMax(condition_18)
condition_18['control'] = '1'

condition_19 = pd.read_csv('condition_19.csv')
condition_19 = condition_19
condition_19['maxMinusMin'] = ""
condition_19 = minMax(condition_19)
condition_19['control'] = '1'

condition_20 = pd.read_csv('condition_20.csv')
condition_20 = condition_20
condition_20['maxMinusMin'] = ""
condition_20 = minMax(condition_20)
condition_20['control'] = '1'

condition_21 = pd.read_csv('condition_21.csv')
condition_21 = condition_21
condition_21['maxMinusMin'] = ""
condition_21 = minMax(condition_21)
condition_21['control'] = '1'

condition_22 = pd.read_csv('condition_22.csv')
condition_22 = condition_22
condition_22['maxMinusMin'] = ""
condition_22 = minMax(condition_22)
condition_22['control'] = '1'

condition_23 = pd.read_csv('condition_23.csv')
condition_23 = condition_23
condition_23['maxMinusMin'] = ""
condition_23 = minMax(condition_23)
condition_23['control'] = '1'

condition_new = condition_1.append(condition_2).append(condition_3).append(condition_4).append(condition_5).append(condition_6).append(condition_7).append(condition_8).append(condition_9).append(condition_10).append(condition_11).append(condition_12).append(condition_13).append(condition_14).append(condition_15).append(condition_16).append(condition_17).append(condition_18).append(condition_19).append(condition_20).append(condition_21).append(condition_22).append(condition_23)
condition_new.to_csv("condition_new.csv")

control_1 = pd.read_csv('control_1.csv')
control_1 = control_1
control_1['maxMinusMin'] = ""
control_1 = minMax(control_1)
control_1['control'] = '0'

control_2 = pd.read_csv('control_2.csv')
control_2 = control_2
control_2['maxMinusMin'] = ""
control_2 = minMax(control_2)
control_2['control'] = '0'

control_3 = pd.read_csv('control_3.csv')
control_3 = control_3
control_3['maxMinusMin'] = ""
control_3 = minMax(control_3)
control_3['control'] = '0'

control_4 = pd.read_csv('control_4.csv')
control_4 = control_4
control_4['maxMinusMin'] = ""
control_4 = minMax(control_4)
control_4['control'] = '0'

control_5 = pd.read_csv('control_5.csv')
control_5 = control_5
control_5['maxMinusMin'] = ""
control_5 = minMax(control_5)
control_5['control'] = '0'

control_6 = pd.read_csv('control_6.csv')
control_6 = control_6
control_6['maxMinusMin'] = ""
control_6 = minMax(control_6)
control_6['control'] = '0'

control_7 = pd.read_csv('control_7.csv')
control_7 = control_7
control_7['maxMinusMin'] = ""
control_7 = minMax(control_7)
control_7['control'] = '0'

control_8 = pd.read_csv('control_8.csv')
control_8 = control_8
control_8['maxMinusMin'] = ""
control_8 = minMax(control_8)
control_8['control'] = '0'

control_9 = pd.read_csv('control_9.csv')
control_9 = control_9
control_9['maxMinusMin'] = ""
control_9 = minMax(control_9)
control_9['control'] = '0'

control_10 = pd.read_csv('control_10.csv')
control_10 = control_10
control_10['maxMinusMin'] = ""
control_10 = minMax(control_10)
control_10['control'] = '0'

control_11 = pd.read_csv('control_11.csv')
control_11 = control_11
control_11['maxMinusMin'] = ""
control_11 = minMax(control_11)
control_11['control'] = '0'

control_12 = pd.read_csv('control_12.csv')
control_12 = control_12
control_12['maxMinusMin'] = ""
control_12 = minMax(control_12)
control_12['control'] = '0'

control_13 = pd.read_csv('control_13.csv')
control_13 = control_13
control_13['maxMinusMin'] = ""
control_13 = minMax(control_13)
control_13['control'] = '0'

control_14 = pd.read_csv('control_14.csv')
control_14 = control_14
control_14['maxMinusMin'] = ""
control_14 = minMax(control_14)
control_14['control'] = '0'

control_15 = pd.read_csv('control_15.csv')
control_15 = control_15
control_15['maxMinusMin'] = ""
control_15 = minMax(control_15)
control_15['control'] = '0'

control_16 = pd.read_csv('control_16.csv')
control_16 = control_16
control_16['maxMinusMin'] = ""
control_16 = minMax(control_16)
control_16['control'] = '0'

control_17 = pd.read_csv('control_17.csv')
control_17 = control_17
control_17['maxMinusMin'] = ""
control_17 = minMax(control_17)
control_17['control'] = '0'

control_18 = pd.read_csv('control_18.csv')
control_18 = control_18
control_18['maxMinusMin'] = ""
control_18 = minMax(control_18)
control_18['control'] = '0'

control_19 = pd.read_csv('control_19.csv')
control_19 = control_19
control_19['maxMinusMin'] = ""
control_19 = minMax(control_19)
control_19['control'] = '0'

control_20 = pd.read_csv('control_20.csv')
control_20 = control_20
control_20['maxMinusMin'] = ""
control_20 = minMax(control_20)
control_20['control'] = '0'

control_21 = pd.read_csv('control_21.csv')
control_21 = control_21
control_21['maxMinusMin'] = ""
control_21 = minMax(control_21)
control_21['control'] = '0'

control_22 = pd.read_csv('control_22.csv')
control_22 = control_22
control_22['maxMinusMin'] = ""
control_22 = minMax(control_22)
control_22['control'] = '0'

control_23 = pd.read_csv('control_23.csv')
control_23 = control_23
control_23['maxMinusMin'] = ""
control_23 = minMax(control_23)
control_23['control'] = '0'

control_24 = pd.read_csv('control_24.csv')
control_24 = control_24
control_24['maxMinusMin'] = ""
control_24 = minMax(control_24)
control_24['control'] = '0'

control_25 = pd.read_csv('control_25.csv')
control_25 = control_25
control_25['maxMinusMin'] = ""
control_25 = minMax(control_25)
control_25['control'] = '0'

control_26 = pd.read_csv('control_26.csv')
control_26 = control_26
control_26['maxMinusMin'] = ""
control_26 = minMax(control_26)
control_26['control'] = '0'

control_27 = pd.read_csv('control_27.csv')
control_27 = control_27
control_27['maxMinusMin'] = ""
control_27 = minMax(control_27)
control_27['control'] = '0'

control_28 = pd.read_csv('control_28.csv')
control_28 = control_28
control_28['maxMinusMin'] = ""
control_28 = minMax(control_28)
control_28['control'] = '0'

control_29 = pd.read_csv('control_29.csv')
control_29 = control_29
control_29['maxMinusMin'] = ""
control_29 = minMax(control_29)
control_29['control'] = '0'

control_30 = pd.read_csv('control_30.csv')
control_30 = control_30
control_30['maxMinusMin'] = ""
control_30 = minMax(control_30)
control_30['control'] = '0'

control_31 = pd.read_csv('control_31.csv')
control_31 = control_31
control_31['maxMinusMin'] = ""
control_31 = minMax(control_31)
control_31['control'] = '0'


control_32 = pd.read_csv('control_32.csv')
control_32 = control_32
control_32['maxMinusMin'] = ""
print("FØR MINMAX() ",control_32)
control_32 = minMax(control_32)
control_32['control'] = '0'

print("ETTER MINMAX() ",control_32)

condition_control = control_1.append(control_2).append(control_3).append(control_4).append(control_5).append(control_6).append(control_7).append(control_8).append(control_9).append(control_10).append(control_11).append(control_12).append(control_13).append(control_14).append(control_15).append(control_16).append(control_17).append(control_18).append(control_19).append(control_20).append(control_21).append(control_22).append(control_23).append(control_24).append(control_25).append(control_26).append(control_27).append(control_28).append(control_29).append(control_30).append(control_31).append(control_32)



condition_control.to_csv("condition_control.csv")