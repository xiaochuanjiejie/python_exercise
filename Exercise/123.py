__author__ = 'xujunchuan'
import os
if os.path.exists('/tmp/scripts/checkThird'):
    pass
else:
    # os.makedirs('/usr/local/LeMonitor/scripts/checkThird')
    # with open('/usr/local/LeMonitor/scripts/checkThird/domain','w') as f:
    #     f.write('{''"domains": []''}''\n')
    os.makedirs('/tmp/scripts/checkThird')
    with open('/tmp/scripts/checkThird/domain','w') as f:
        f.write('{''"domains": []''}''\n')
