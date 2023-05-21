
# Login Form Scenario
def test_login_form():
    # Test cases for Login Form
    login_form_test_cases = [
        {
            'username': 'testuser',
            'password': 'testpassword',
            'expected_result': 'success'
        },
        {
            'username': 'testuser',
            'password': '',
            'expected_result': 'failure'
        },
        {
            'username': '',
            'password': 'testpassword',
            'expected_result': 'failure'
        }
    ]

    # Execute and compare test results for Login Form
    login_form_results = []
    for case in login_form_test_cases:
        # Execute test case logic
        result = None
        if case['username'] == 'testuser' and case['password'] == 'testpassword':
            result = 'success'
        else:
            result = 'failure'

        # Compare expected and actual results
        if result == case['expected_result']:
            login_form_results.append('PASSED')
        else:
            login_form_results.append('FAILED')

    # Print the test results for Login Form
    print('Login Form Test Results:')
    for index, result in enumerate(login_form_results):
        print('Test Case {}: {}'.format(index+1, result))

# E-commerce Shopping Cart Scenario
def test_shopping_cart():
    # Test cases for E-commerce Shopping Cart
    shopping_cart_test_cases = [
        {
            'item': 'Product A',
            'quantity': 2,
            'expected_result': 'success'
        },
        {
            'item': 'Product B',
            'quantity': 0,
            'expected_result': 'failure'
        },
        {
            'item': '',
            'quantity': 2,
            'expected_result': 'failure'
        }
    ]

    # Execute and compare test results for E-commerce Shopping Cart
    shopping_cart_results = []
    for case in shopping_cart_test_cases:
        # Execute test case logic
        result = None
        if case['item'] != '' and case['quantity'] > 0:
            result = 'success'
        else:
            result = 'failure'

        # Compare expected and actual results
        if result == case['expected_result']:
            shopping_cart_results.append('PASSED')
        else:
            shopping_cart_results.append('FAILED')

    # Print the test results for E-commerce Shopping Cart
    print('Shopping Cart Test Results:')
    for index, result in enumerate(shopping_cart_results):
        print('Test Case {}: {}'.format(index+1, result))

# Social Media Profile Scenario
def test_social_media_profile():
    # Test cases for Social Media Profile
    profile_test_cases = [
        {
            'name': 'John Doe',
            'bio': 'Test bio',
            'location': 'Test location',
            'expected_result': 'success'
        },
        {
            'name': '',
            'bio': '',
            'location': '',
            'expected_result': 'failure'
        }
    ]
    # Execute and compare test results for Social Media Profile
    profile_results = []
    for case in profile_test_cases:
        # Execute test case logic
        result = None
        if case['name'] != '' or case['bio'] != '' or case['location'] != '':
            result = 'success'
        else:
            result = 'failure'

        # Compare expected and actual results
        if result == case['expected_result']:
            profile_results.append('PASSED')
        else:
            profile_results.append('FAILED')

    # Print the test results for Social Media Profile
    print('Social Media Profile Results:')
    for index, result in enumerate(profile_results):
        print('Test Case {}: {}'.format(index+1, result))
