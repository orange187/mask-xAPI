#使用pytest.fixture
import pytest
@pytest.fixture(scope='function',params=['http://3.84.114.207/'])
def my_fixture(request):
    print('前置')
    yield request.param  #yield返回
    print('后置')