import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

    # Test 1: The allowed number of characters (1)
def test_create_kit_name_1_character():
    new_kit_body = get_kit_body("a")
    positive_assert(new_kit_body)

# Test 2: The allowed number of characters (511)
def test_create_kit_name_511_character():
    new_kit_body = get_kit_body(data.kit_name_511_chars)
    positive_assert(new_kit_body)

# Test 3: Number of characters less than allowed (0)
def test_create_kit_name_0_character():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

# Test 4: Number of characters greater than allowed (512)
def test_create_kit_name_512_character():
    new_kit_body = get_kit_body(data.kit_name_512_chars)
    negative_assert_code_400(new_kit_body)

# Test 5: Special characters allowed
def test_create_kit_name_special_character():
    new_kit_body = get_kit_body("\"№%@\",")
    positive_assert(new_kit_body)

# Test 6: Spaces are allowed
def test_create_kit_spaces_in_name():
    new_kit_body = get_kit_body("A Aaa")
    positive_assert(new_kit_body)

# Test 7: Number are allowed
def test_create_kit_number_iin_name():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

# Test 8: The parameter is not passed in the request
def test_create_kit_no_name_parameter():
    new_kit_body = {}
    negative_assert_code_400(new_kit_body)

# Test 9: different parameter type
def test_create_kit_different_type_in_name():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)
