from os import curdir, listdir, path
import pandas as pd

combined_fd = pd.DataFrame()
for csvfile in [x for x in listdir(curdir) if path.isfile(x) and x.endswith('.csv')]:
    fd = pd.read_csv(csvfile, index_col=0)
    with open(csvfile, 'r') as f:
        fd = fd.assign(company=[csvfile.split('.')[0]] * len(fd))
    combined_fd = combined_fd.append(fd)
    fd.to_csv(csvfile, index=False)

combined_fd.to_csv('combined_news.csv')