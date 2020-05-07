# PyCharm -> File -> Setting -> Project -> Project Interpreter
# +: 패키지 인스톨
# cx_oracle 패키지 인스톨

# PyCharm 세팅에서 패키지 인스톨이 안되는 경우
# Anaconda 프롬프트(base)
# > pip install cx_oracle --upgrade

import cx_Oracle

print(cx_Oracle.__version__)
