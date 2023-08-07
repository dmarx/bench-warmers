# Pandas Wrangler

![](https://img.shields.io/badge/tag-tooling-lightgrey)


inspired by: https://www.reddit.com/r/Python/comments/11fio85/we_are_the_developers_behind_pandas_currently/jajz9a0/?context=3

```python

import pandas as pd
import pandas_wrangler

pandas_wrangler.patch()

df._ \
  .sane_api \
  .patched_in_sneakily \
  .by_hacking_the_namespace()
```

backwards compatibility preserved by just creating an alternate api that links around. Something like:


```python
class DataFrame:
    ...
    def somefunction(self)
        # namespace package?
        from .dataframe._.sane_api.module.submodule import somefunction as somefunction_
        return somefunction_(self)
```

which would then permit both old style usage -- `df.somefunction()` -- as well as more functional use -- `from sane_api.module.submodule import somefunction; somefunction(df)` -- and/or -- `df._.sane_api.module.submodule.somefunction()`
