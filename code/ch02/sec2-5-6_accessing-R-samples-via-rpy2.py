# -*- coding: utf-8 -*-
# 2.5.6節  scikit-learn や R のサンプルデータ　　Rのサンプルデータをアクセスする
from rpy2.robjects import pandas2ri
pandas2ri.activate()    # あらかじめactivateしておく
from rpy2.robjects import r
irisdf = r["iris"]      # Rのirisデータがirisdfに読み込まれる
titanic = r["Titanic"]  # RのTitanicデータがtitanicに読み込まれる

print(irisdf)
print(titanic)
