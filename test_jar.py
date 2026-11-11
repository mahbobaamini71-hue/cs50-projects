from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12  
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar('One')
    with pytest.raises(ValueError):
        Jar(1.2)
        

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(9)
    assert jar.size == 9
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(2)
    assert jar.size == 11    
    with pytest.raises(ValueError):
        jar.deposit(13)



def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
        
    jar.deposit(8)
    jar.withdraw(2)
    assert jar.size == 6
    
    with pytest.raises(ValueError):
        jar.withdraw(7)
