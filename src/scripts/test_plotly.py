import cufflinks as cf
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from plotly import __version__
from plotly.offline import init_notebook_mode, plot, iplot

print(__version__)
init_notebook_mode(connected=True)
cf.go_offline()

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})

plot(px.line(df))
iplot(px.line(df))
# plt.show()
