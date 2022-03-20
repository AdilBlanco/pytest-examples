import random
from unittest.mock import Mock, patch


class Programmer:

    def __init__(self):
        self.tech_names = []

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if not name in self.tech_names:
            self.tech_names.append(name)
            return self
        return self

    def get_random_tech(self):
        return random.choice(self.tech_names)


programmer = Programmer().add_tech('python') \
    .add_tech('java') \
    .add_tech('sql') \
    .add_tech('aws') \
    .add_tech('django')


# Mock
# ******
random.choice = Mock(return_value="python")
print(random.choice.call_count)
print(programmer.get_random_tech())
print(random.choice.call_count)

print("\n")

# how to mock
with patch("random.choice", return_value="sql"):
    print(random.choice.call_count)
    print(programmer.get_random_tech())
    print(random.choice.call_count)

# how to mock
with patch('random.choice') as mock_random:
    mock_random.return_value = 'sql'
    print(programmer.get_random_tech())
    print(random.choice.call_count)

# how to mock

@patch('random.choice')
def test_get_random_tech(mock_random):
    mock_random.return_value = 'sql'
    return programmer.get_random_tech()
