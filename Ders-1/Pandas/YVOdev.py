import numpy as np
import pandas as pd

videos=pd.read_csv("./USvideos.csv")


#Silem 
#df=videos.drop(["thumbnail_link","video_id","trending_date","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1)

countindex=len(videos.index)
countcolumn=len(videos.columns)
print("İndex:{},Column:{}".format(countindex,countcolumn))