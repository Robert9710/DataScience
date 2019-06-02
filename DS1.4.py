# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
#print(DF_obj)

DF_obj2 = pd.DataFrame(np.arange(15).reshape(5,3))
#print(DF_obj2)

#print(pd.concat([DF_obj, DF_obj2], axis=1))

"""Drop the specified rows"""
#print(DF_obj.drop([0,2]))

#print(DF_obj.drop([0,2], axis=1))

series_obj=Series(np.arange(6))
series_obj.name = "added_variable"
#print(series_obj)

variable_added=DataFrame.join(DF_obj, series_obj)
#print(variable_added)

added_datatable=variable_added.append(variable_added, ignore_index=True)
#print(added_datatable)

DF_sorted=DF_obj.sort_values(by=[5], ascending=[False])
print(DF_obj)
print(DF_sorted)





