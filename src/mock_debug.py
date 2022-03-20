import random
from unittest.mock import Mock


techs = ['python', 'aws', 'c++']

random.choice = Mock(return_value='aws')
print(random.choice.return_value)
print(random.choice.call_count)

random.choice(techs)
print(random.choice.call_count)
